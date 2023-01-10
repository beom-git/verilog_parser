import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import re
from lib.vlog_keyword import *
from lib.vlog_regex import *


class parser_vlog():

    def __init__(self, file_name : str):
        self.file_name = file_name
        self.vlog_tag_each_line    = []
        self.vlog_include_list     = []
        self.vlog_define_list      = []
        self.vlog_module_list      = []
        self.vlog_port_list        = []
        self.vlog_net_list         = []
        self.vlog_reg_list         = []
        self.vlog_paramter_list    = []
        self.vlog_localparam_list  = []
        self.vlog_assign_list      = []
        self.vlog_instance_list    = []

    ## Step 1 : make Tag
    ## make tag of all line with keyword
    def get_vlog_analysis(self):
        idx = 0
        with open(self.file_name, "r") as read_vlog:
            lines = read_vlog.readlines()
            for line in lines:
                self.get_vlog_keyword(idx, line)
                idx+=1

    ## get keyword by regexp
    def get_vlog_keyword(self, vlog_line_idx: int, vlog_line: str):
        for key, value in dict_vlog_keyword.items():
            IsValid = self.discovery_vlog_keyword(value, vlog_line)
            if(IsValid): self.vlog_tag_each_line += [[key, vlog_line_idx, vlog_line]]
    
    ## keyword match
    def discovery_vlog_keyword(self, regexp: str, vlog_line: str):
        re_compiled = re.compile(regexp)
        re_object   = re_compiled.match(vlog_line)
        IsValid     = True if(re_object) else False
        return IsValid

    ## for debugging
    def show_vlog_anlysis(self):
        for idx in range(len(self.vlog_tag_each_line)):
            print(self.vlog_tag_each_line[idx])

    ## Step #2 : extract information
    ## 
    def parsing_include(self):
        for line_tag in self.vlog_tag_each_line:
            if(line_tag[0]=="include"):
                re_obj = re.search(r'(\w*)\.(v|sv|vh|svh)', line_tag[2])
                inc_file_name = re_obj.group()
                self.vlog_include_list += [[line_tag[1], inc_file_name]]

    def parsing_define(self):
        for line_tag in self.vlog_tag_each_line:
            if(line_tag[0]=="define"):
                re_obj = re.search(r'(`define)(\s*)(\w*)(\s*)(\w*)', line_tag[2])
                inc_file_name = re_obj.groups()
                self.vlog_include_list += [[line_tag[1], inc_file_name]]




    #def extract_regexp( regexp : str, vlog_line : str ):
    #    re_compiled    = re.compile(regexp)
    #    re_object      = re_compiled.match(vlog_line)
    #    Match_String   = re_object.group() if(re_object) else None
    #    Match_Span     = re_object.span()  if(re_object) else (None, None) 

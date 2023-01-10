## regex - match keyword line
dict_vlog_keyword = {
    "define"       : "^(\s*)?`define(\s*)"    , 
    "include"      : "^(\s*)?`include(\s*)"   , 
    "module"       : "^(\s*)?module(\s*)"     ,
    "port"         : "^(\s*)?(input|output|inout)(\s*)" ,
    "net"          : "^(\s*)?wire(\s*)"       ,
    "reg"          : "^(\s*)?reg(\s*)"        ,
    "paramter"     : "^(\s*)?paramter(\s*)"   ,
    "localparam"   : "^(\s*)?localparam(\s*)" ,
    "assignment"   : "^(\s*)?assign(\s*)" 
}

## regex - math keyword single line
dict_re_sigle_line = {
    "re_define"       : "^(\s*)?`define(\s*)\w*(\s*)\w*" , ## single line define
    "re_include"      : "^(\s*)?`include(\s*)\"(\w*)\.(v|sv|vh|svh)\"" , ## file_format = .vh, .svh, .v, .sv
    "re_module"       : "^(\s*)?module(\s*)\w*" ,
    "re_port"         : "^(\s*)?(input|output|inout)(\s*)(wire|reg)(\s*)?(\[\w*:\w\])?(\s*)?\w*;" ,
    "re_net"          : "^(\s*)?wire(\s*)(\[\w*:\w\])?(\s*)?(\w*);" ,
    "re_reg"          : "^(\s*)?reg(\s*)(\[\w*:\w\])?(\s*)?(\w*)(\s*)?(\[\w*:\w\])?;" ,
    "re_paramter"     : "^(\s*)?paramter(\s*)(\[\w*:\d\])?(\s*)?(\w*)?;" ,
    "re_localparam"   : "^(\s*)?localparam(\s*)(\[\w*:\w\])?(\s*)?(\w*)?;" ,
    "re_assignment"   : "^(\s*)?assign(\s*)(\w*)(\[+((\w:\w)|(\w))+\])?(\s*)?=(\s*)?(\w*)(\[((\w*:\w)|(\w))\])?(\s*)?;"  # Support that up to 2-Demesion
}
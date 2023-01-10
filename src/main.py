from parsing_verilog import *
from config import *


if (__name__ == "__main__") :
    parser_vlog_tmp = parser_vlog(SAMPLE_FILE_PATH+"tmp.v")
    parser_vlog_tmp.get_vlog_analysis()
    parser_vlog_tmp.show_vlog_anlysis()
    
    parser_vlog_tmp.parsing_include()
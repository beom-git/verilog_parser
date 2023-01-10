## each reserved keyword list
vlog1995_keyword = [
	"always"      , "ifnone"     , "rpmos"       , "and"          , "initial"  ,
	"rtran"       , "assign"     , "inout"       , "rtranif0"     , "begin"    ,
	"input"       , "rtranif1"   , "buf"         , "integer"      , "scalared" ,
	"bufif0"      , "join"       , "small"       , "bufif1"       , "large"    ,
	"specify"     , "case"       , "macromodule" , "specparam"    , "casex"    ,
	"medium"      , "strong0"    , "casez"       , "module"       , "strong1"  ,
	"cmos"        , "nand"       , "supply0"     , "deassign"     , "negedge"  ,
	"supply1"     , "default"    , "nmos"        , "table"        , "defparam" ,
	"nor"         , "task"       , "disable"     , "not"          , "time"     ,
	"edge"        , "notif0"     , "tran"        , "else"         , "notif1"   ,
	"tranif0"     , "end"        , "or"          , "tranif1"      , "endcase"  ,
	"output"      , "tri"        , "endmodule"   , "parameter"    , "tri0"     ,
	"endfunction" , "pmos"       , "tri1"        , "endprimitive" , "posedge"  ,
	"triand"      , "endspecify" , "primitive"   , "trior"        , "endtable" ,
	"pull0"       , "trireg"     , "endtask"     , "pull1"        , "vectored" ,
	"event"       , "pullup"     , "wait"        , "for"          , "pulldown" ,
	"wand"        , "force"      , "rcmos"       , "weak0"        , "forever"  ,
	"real"        , "weak1"      , "fork"        , "realtime"     , "while"    ,
	"function"    , "reg"        , "wire"        , "highz0"       , "release"  ,
	"wor"         , "highz1"     , "repeat"      , "xnor"         , "if"       ,
	"rnmos"       , "xor"
]

vlog2001_keyword = [
"automatic"          , "incdir"        , "pulsestyle_ondetect" , "cell"    , "include"         ,
"pulsestyle_onevent" , "config"        , "instance"            , "signed"  , "endconfig"       ,
"liblist"            , "showcancelled" , "endgenerate"         , "library" , "unsigned"        ,
"generate"           , "localparam"    , "use"                 , "genvar"  , "noshowcancelled"
]


systemvlog_keyword = [
"accept_on"    , "export"         , "ref"          , "alias"          , "extends"      ,
"restrict"     , "always_comb"    , "extern"       , "return"         , "always_ff"    ,
"final"        , "s_always"       , "always_latch" , "first_match"    , "s_eventually" ,
"assert"       , "foreach"        , "s_nexttime"   , "assume"         , "forkjoin"     ,
"s_until"      , "before"         , "global"       , "s_until_with"   , "bind"         ,
"iff"          , "sequence"       , "bins"         , "ignore_bins"    , "shortint"     ,
"binsof"       , "illegal_bins"   , "shortreal"    , "bit"            , "implies"      ,
"solve"        , "break"          , "import"       , "static"         , "byte"         ,
"inside"       , "string"         , "chandle"      , "int"            , "strong"       ,
"checker"      , "interface"      , "struct"       , "class"          , "intersect"    ,
"super"        , "clocking"       , "join_any"     , "sync_accept_on" , "const"        ,
"join_none"    , "sync_reject_on" , "constraint"   , "let"            , "tagged"       ,
"context"      , "local"          , "this"         , "continue"       , "logic"        ,
"throughout"   , "cover"          , "longint"      , "timeprecision"  , "covergroup"   ,
"matches"      , "timeunit"       , "coverpoint"   , "modport"        , "type"         ,
"cross"        , "new"            , "typedef"      , "dist"           , "nexttime"     ,
"union"        , "do"             , "null"         , "unique"         , "endchecker"   ,
"package"      , "unique0"        , "endclass"     , "packed"         , "until"        ,
"endclocking"  , "priority"       , "until_with"   , "endgroup"       , "program"      ,
"untypted"     , "endinterface"   , "property"     , "var"            , "endpackage"   ,
"protected"    , "virtual"        , "endprogram"   , "pure"           , "void"         ,
"endproperty"  , "rand"           , "wait_order"   , "endsequence"    , "randc"        ,
"weak"         , "enum"           , "randcase"     , "wildcard"       , "eventually"   ,
"randsequence" , "with"           , "expect"       , "reject_on"      , "within"
]

## all reserved keyword list
vlog_all_keyword   = vlog1995_keyword+vlog2001_keyword+systemvlog_keyword

## regex - match keyword line
dict_vlog_keyword = {
    "define"       : "^(\s*)?`define(\s*)"    , 
    "include"      : "^(\s*)?`include(\s*)"   , 
    "module"       : "^(\s*)?module(\s*)"     ,
    "input"        : "^(\s*)?input(\s*)"      ,
    "output"       : "^(\s*)?output(\s*)"     ,
    "inout"        : "^(\s*)?input(\s*)"      ,
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
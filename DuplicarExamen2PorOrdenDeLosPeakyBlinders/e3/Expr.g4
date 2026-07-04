grammar Expr;

root: xml EOF;

xml: '<' TAG_NAME '>' content '</' TAG_NAME '>'
   | '<' TAG_NAME '/>'
   ;

content: (TEXT | xml)* ;

TAG_NAME: [A-Za-z][A-Za-z0-9_-]* ;
TEXT: ~[<]+ ;
WS: [ \t\r\n]+ -> skip ;
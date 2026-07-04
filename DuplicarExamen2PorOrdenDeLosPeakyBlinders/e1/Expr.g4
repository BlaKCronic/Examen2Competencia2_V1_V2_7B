grammar Expr;

program: (classDeclaration | methodDeclaration | statement | importDeclaration)* EOF;

importDeclaration: 'import' ID ('.' ID)* ';';
classDeclaration: 'class' ID ('extends' ID)? '{' classBody* '}';
classBody: fieldDeclaration | methodDeclaration | constructorDeclaration | classDeclaration;

fieldDeclaration: type ID ('=' expression)? ';';
methodDeclaration: accessModifier? 'static'? type ID '(' parameterList? ')' block;
constructorDeclaration: accessModifier? ID '(' parameterList? ')' block;
parameterList: parameter (',' parameter)*;
parameter: type ID;

type: primitiveType | ID | type '[' ']';
primitiveType: 'int' | 'double' | 'String' | 'boolean' | 'Boolean';

block: '{' statement* '}';
statement: variableDeclaration
    | assignment
    | printStatement
    | scannerDeclaration
    | loopStatement
    | returnStatement
    | methodCall
    | ';';

variableDeclaration: type ID ('=' expression)? ';';
assignment: ID '=' expression ';';
printStatement: 'System.out.println' '(' expression ')' ';';
scannerDeclaration: 'Scanner' ID '=' 'new' 'Scanner' '(' 'System.in' ')' ';';
loopStatement: forLoop | whileLoop | doWhileLoop;
forLoop: 'for' '(' variableDeclaration? ';' expression? ';' assignment? ')' block;
whileLoop: 'while' '(' expression ')' block;
doWhileLoop: 'do' block 'while' '(' expression ')' ';';
returnStatement: 'return' expression? ';';
methodCall: ID '(' arguments? ')' ';';
arguments: expression (',' expression)*;
expression: ID | STRING | NUMBER | expression ('+' | '-' | '*' | '/') expression;

accessModifier: 'public' | 'private' | 'protected';

ID: [a-zA-Z_][a-zA-Z0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ ->skip;

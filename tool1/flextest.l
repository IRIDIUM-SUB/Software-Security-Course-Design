/*See https://blog.csdn.net/u014594922/article/details/51224231*/
/*See https://pandolia.net/tinyc/ch8_flex.html#flex-tinyc */
/*Issue:VAR覆盖了所有的关键字*/
/*Solved*/
%%

auto {return 0;}
break {return 1;}
case {return 2;}
char {return 3;}
const {return 4;}
continue  {return 5;}
default   {return 6;}
do    {return 7;}
double    {return 8;}
else  {return 9;}
enum  {return 10;}
extern    {return 11;}
float {return 12;}
for   {return 13;}
goto  {return 14;}
if    {return 15;}
inline    {return 16;}
int   {return 17;}
long  {return 18;}
register  {return 19;}
return    {return 20;}
short {return 21;}
signed    {return 22;}
sizeof    {return 23;}
static    {return 24;}
struct    {return 25;}
switch    {return 26;}
typedef   {return 27;}
union    {return 28;}
unsigned    {return 86;}
void    {return 87;}
volatile    {return 88;}
while    {return 89;}

(\()    {return 30;}
(\))   {return 31;}
(\[)   {return 32;}
(\])   {return 33;}
(\-\>)   {return 34;}
(\.)   {return 35;}
(!)   {return 36;}
(~)   {return 37;}
(\+\+)   {return 38;}
(\-\-)   {return 39;}
(\-)   {return 40;}
(\*)   {return 41;}
(&)   {return 42;}
(\/)   {return 43;}
(%)   {return 44;}
(\+)   {return 45;}
(\<\<)   {return 46;}
(\>\>)   {return 47;}
(\<)   {return 48;}
(\<=)   {return 49;}
(\>)   {return 50;}
(\>=)   {return 51;}
(==)   {return 52;}
(!=)   {return 53;}
(\^)   {return 54;}
(\|)   {return 55;}
(&&)   {return 56;}
(\|\|)   {return 57;}
(\?:)   {return 58;}
(=)   {return 59;}
(\+=)   {return 60;}
(\-=)   {return 61;}
(\*=)   {return 62;}
(\/=)   {return 63;}
(%=)   {return 64;}
(\>\>=)   {return 65;}
(\<\<=)   {return 66;}
(&=)   {return 67;}
(\^=)   {return 68;}
(\|=)   {return 69;}
(,)   {return 70;}
(\\a)   {return 71;}
(\\b)   {return 72;}
(\\f)   {return 73;}
(\\n)   {return 74;}
(\\r)   {return 75;}
(\\t)   {return 76;}
(\\v)   {return 77;}
(;)   {return 78;}
(:)   {return 79;}
(\+|\-)?([1-9][0-9]*|0)   {return 80;}
(\+|\-)?([1-9][0-9]*|0)(\.[0-9]+)   {return 81;}
(')([a-z]|[A-Z])(')   {return 82;}
(")([\s\S]*)(")   {return 83;}
(\/\/)   {return 84;}
(\/\*)([\s\S]*)(\*\/)   {return 85;}
(([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|_)*) {return 29;}

%%
static char* print_token(int token) {
static char* token_strs[] = {"$AUTO","$BREAK","$CASE","$CHAR","$CONST","$CONTINUE","$DEFAULT","$DO","$DOUBLE","$ELSE","$ENUM","$EXTERN","$FLOAT","$FOR","$GOTO","$IF","$INLINE","$INT","$LONG","$REG","$RET","$SHORT","$SIGNED","$SIZEOF","$STATIC","$STRUCT","$SWITCH","$TYPEDEF","$UNION","$VAR","$LROUND","$RROUND","$LSQUARE","$RSQUARE","$ARROW","$DOT","$NOT","$BITREV","$SELFADD","$SELFSUB","$MINUS","$MUL","$BITAND","$DIV","$MOD","$ADD","$SL","$SR","$LE","$LEQ","$MO","$MEQ","$EQU","$NEQU","$BITXOR","$BITOR","$AND","$OR","$TRIOP","$IS","$ISADD","$ISMINU","$ISMUL","$ISDIV","$ISMOD","$ISSR","$ISSL","$ISBITAND","$ISBITXOR","$ISBITOR","$COMMA","$BELL","$BORDER","$PAGE","$NEWLINE","$CR","$TAB","$VT","$SEMI","$COLON","$CONSINT","$CONSFLOAT","$CONSCHAR","$CONSSTR","$SINGLELINECOMMENT","$BLOCKCOMMENT", "$UNSIGNED","$VOID","$VOL", "$WHILE"};
//printf("%-20s", token_strs[token]);
return token_strs[token];
}

int main(int argc,char** argv)
{
    int tok;
    while(tok=yylex())
    {
       printf("%s",print_token(tok));
    }
    return 0;
}

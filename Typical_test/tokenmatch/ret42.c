int main(int argc,char** argv){

int res= foo(argc);
if (res==42)
{
    return 1;
}
else
{
    return 0;
}

}
int foo(int para)
{
    if (para==1)
    return 42;
    else
    {
        return 43;
    }
    
}
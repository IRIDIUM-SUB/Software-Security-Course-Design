int main(int argc,char** argv)
{

int kpr= bug(argc);
if (kpr==42)
{
    return 1;
}
else
{
    return 0;
}
}
int bug(int parb)
{
    if (parb==1)
    return 42;
    else
    {
        return 43;
    }
    
}
/*Used for test 1*/
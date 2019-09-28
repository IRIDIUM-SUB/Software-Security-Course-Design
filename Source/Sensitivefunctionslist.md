
[@TOC]
# Sensitive function:

- `char *strcpy(char* dest, const char *src);`
- `char *strncpy(char *destinin, char *source, int maxlen);`
- `void *memcpy(void *destin, void *source, unsigned n);`
- `char *strcat(char *dest, const char *src);`
- ` char *strncat (char *dest,char *src,int n)`
- `int sprintf ( char * str, const char * format, ... );`
- `int vsprintf(char *str, const char *format, va_list arg) `
- `char * gets ( char * str )`
- `int getchar(void)`
- `int fgetc(FILE *stream)`
- `int getc(FILE * stream)`
- `ssize_t read(int fd, void * buf, size_t count); `
- `int sscanf(const char *str, const char *format, ...) `
- `int fscanf(FILE *stream, const char *format, ...)`
- `int vfscanf(FILE * stream, const char * format, va_list ap);`
- `int vscanf ( const char * format, va_list arg );`
- `int vsscanf ( const char * s, const char * format, va_list arg );`

## strncpy:
```
r"(strncpy\([\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+\))|(strncpy\([\*&]*[a-zA-Z1-9_0]+,"[\s\S]+"+,[\*&]*[a-zA-Z1-9_0]+\))"
```
## strcpy
```
r"(strcpy\([\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+\))|(strcpy\([\*&]*[a-zA-Z1-9_0]+,"[\s\S]+"+\))"
```
## memcpy
```
r"(memcpy\([\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+\))|(memcpy\([\*&]*[a-zA-Z1-9_0]+,"[\s\S]+"+,[\*&]*[a-zA-Z1-9_0]+\))"
```


## gets
```
r"gets\([\*&]*[a-zA-Z1-9_0]+\)"
```
## getc
```
r"[\*&]*[a-zA-Z1-9_0]+\s*=\s*getc\([\s\S]*\)"
```
## strcat
```
r"(strcat\([\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+\))|(strcat\([\*&]*[a-zA-Z1-9_0]+,"[\s\S]+"+\))"
```
## strncat
```
r"(strncat\([\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+,[\*&]*[a-zA-Z1-9_0]+\))|(strncat\([\*&]*[a-zA-Z1-9_0]+,"[\s\S]+"+,[\*&]*[a-zA-Z1-9_0]+\))"
```
## sprintf
```
r"(sprintf\([\*&]*[a-zA-Z1-9_0]+,[\s\S]*\))|(sprintf\([\*&]*[a-zA-Z1-9_0]+,[\s\S]*\))"
```
## getchar
```
r"[\*&]*[a-zA-Z1-9_0]+\s*=\s*getchar\(\)"
```
{

  "title": "The method newInstance() from the type Class is deprecated since version 9",
  "date": "2019-10-14",
  "description": "newInstance()在 java9中已被弃用 JAVA9之前用法 JAVA9之后用法 源码说明",
  "tags": [
    "JAVA"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11674336.html"

}

newInstance()在 java9中已被弃用

JAVA9之前用法

```text
1 Class.forName("类的全限定名").newInstance();
```

JAVA9之后用法

```text
1 Class.forName("类的全限定名").getDeclaredConstructor().newInstance();
```

源码说明

```text
 1     /**
 2      * Uses the constructor represented by this {@code Constructor} object to
 3      * create and initialize a new instance of the constructor's
 4      * declaring class, with the specified initialization parameters.
 5      * Individual parameters are automatically unwrapped to match
 6      * primitive formal parameters, and both primitive and reference
 7      * parameters are subject to method invocation conversions as necessary.
 8      *
 9      * <p>If the number of formal parameters required by the underlying constructor
10      * is 0, the supplied {@code initargs} array may be of length 0 or null.
11      *
12      * <p>If the constructor's declaring class is an inner class in a
13      * non-static context, the first argument to the constructor needs
14      * to be the enclosing instance; see section 15.9.3 of
15      * <cite>The Java&trade; Language Specification</cite>.
16      *
17      * <p>If the required access and argument checks succeed and the
18      * instantiation will proceed, the constructor's declaring class
19      * is initialized if it has not already been initialized.
20      *
21      * <p>If the constructor completes normally, returns the newly
22      * created and initialized instance.
23      *
24      * @param initargs array of objects to be passed as arguments to
25      * the constructor call; values of primitive types are wrapped in
26      * a wrapper object of the appropriate type (e.g. a {@code float}
27      * in a {@link java.lang.Float Float})
28      *
29      * @return a new object created by calling the constructor
30      * this object represents
31      *
32      * @exception IllegalAccessException    if this {@code Constructor} object
33      *              is enforcing Java language access control and the underlying
34      *              constructor is inaccessible.
35      * @exception IllegalArgumentException  if the number of actual
36      *              and formal parameters differ; if an unwrapping
37      *              conversion for primitive arguments fails; or if,
38      *              after possible unwrapping, a parameter value
39      *              cannot be converted to the corresponding formal
40      *              parameter type by a method invocation conversion; if
41      *              this constructor pertains to an enum type.
42      * @exception InstantiationException    if the class that declares the
43      *              underlying constructor represents an abstract class.
44      * @exception InvocationTargetException if the underlying constructor
45      *              throws an exception.
46      * @exception ExceptionInInitializerError if the initialization provoked
47      *              by this method fails.
48      */
49     @CallerSensitive
50     @ForceInline // to ensure Reflection.getCallerClass optimization
51     public T newInstance(Object ... initargs)
52         throws InstantiationException, IllegalAccessException,
53                IllegalArgumentException, InvocationTargetException
54     {
55         Class<?> caller = override ? null : Reflection.getCallerClass();
56         return newInstanceWithCaller(initargs, !override, caller);
57     }
```

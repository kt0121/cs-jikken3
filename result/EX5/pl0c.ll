@n = common global i32 0, align 4
@x = common global i32 0, align 4
@i = common global i32 0, align 4
define void @prime(){
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = load i32, i32* @x, align 4
 %4 = div nsw i32 %3, 2
 store i32 %4, i32* %2, align 4
 br label %while.init.1
 while.init.1:
 %5 = load i32, i32* @x, align 4
 %6 = load i32, i32* @x, align 4
 %7 = load i32, i32* %2, align 4
 %8 = div nsw i32 %6, %7
 %9 = load i32, i32* %2, align 4
 %10 = mul nsw i32 %8, %9
 %11 = icmp ne i32 %5, %10
 br il %11,label %while.do.1, label %while.end.1
 while.do.1:
 %12 = load i32, i32* %2, align 4
 %13 = sub nsw i32 %12, 1
 store i32 %13, i32* %2, align 4
 br label %while.init.1
 while.end.1:
 %14 = load i32, i32* %2, align 4
 %15 = icmp eq i32 %14, 1
 br il %15,label %if.then.1, label %if.else.1
 if.then.1:
 %16 = load i32, i32* @x, align 4
 %17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.write, i64 0, i64 0), i32 %16)
 br label %if.end.1
 if.else.1:
 br label %if.end.1
 if.end.1:
}
define i32 @main(){
 @.str.write = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
 declare dso_local i32 @printf(i8*, ...) #1
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.read, i64 0, i64 0), i32* %2)
 %4 = load i32, i32* %2, align 4
 store i32 %4, i32* @n, align 4
 %5 = load i32, i32* @n, align 4
 store i32 2, i32* @i, align 4
 br label %for.do.1
 for.cond.1:
 %6 = load i32, i32* @i, align 4
 %7 = add nsw i32 %6, 1
 store i32 %7, i32* @i, align 4
 %8 = icmp sle i32 %7, %5
 br il %8,label %for.do.1, label %for.end.1
 for.do.1:
 %9 = load i32, i32* @i, align 4
 store i32 %9, i32* @x, align 4
 %10 = call i32 @prime
 br label %for.cond.1
 for.end.1:
}

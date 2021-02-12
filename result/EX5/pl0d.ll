@n = common global i32 0, align 4
@temp = common global i32 0, align 4
define void @fact(){
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = load i32, i32* @n, align 4
 %4 = icmp sle i32 %3, 1
 br i1 %4,label %if.then.1, label %if.else.1
 if.then.1:
 store i32 1, i32* @temp, align 4
 br label %if.end.1
 if.else.1:
 %5 = load i32, i32* @n, align 4
 store i32 %5, i32* %2, align 4
 %6 = load i32, i32* @n, align 4
 %7 = sub nsw i32 %6, 1
 store i32 %7, i32* @n, align 4
 %8 = call i32 @fact
 %9 = load i32, i32* @temp, align 4
 %10 = load i32, i32* %2, align 4
 %11 = mul nsw i32 %9, %10
 store i32 %11, i32* @temp, align 4
 br label %if.end.1
 if.end.1:
 ret void
}
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = alloca i32, align 4
 %3 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.read, i64 0, i64 0), i32* %2)
 %4 = load i32, i32* %2, align 4
 store i32 %4, i32* @n, align 4
 %5 = call i32 @fact
 %6 = load i32, i32* @temp, align 4
 %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.write, i64 0, i64 0), i32 %6)
 ret i32 0
}

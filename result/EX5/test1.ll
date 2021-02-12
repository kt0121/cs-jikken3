@x = common global i32 0, align 4
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = mul nsw i32 3, 2
 %3 = add nsw i32 4, %2
 %4 = sub nsw i32 %3, 1
 %5 = mul nsw i32 5, 2
 %6 = add nsw i32 %4, %5
 %7 = mul nsw i32 4, 4
 %8 = sub nsw i32 %6, %7
 %9 = add nsw i32 %8, 20
 %10 = sub nsw i32 %9, 100
 %11 = mul nsw i32 4, 2
 %12 = sdiv i32 %11, 5
 %13 = add nsw i32 %10, %12
 store i32 %13, i32* @x, align 4
ret i32 0
}

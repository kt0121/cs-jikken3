@x = common global i32 0, align 4
define i32 @main(){
 %1 = alloca i32, align 4
 %2 = mul nsw i32 4, 5
 %3 = add nsw i32 2, %2
 %4 = sub nsw i32 %3, 7
 store i32 %4, i32* @x, align 4
ret i32 0
}

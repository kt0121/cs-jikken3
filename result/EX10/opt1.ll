@x = common global i32 0, align 4
define i32 @main(){
 %1 = alloca i32, align 4
 store i32 9, i32* @x, align 4
}

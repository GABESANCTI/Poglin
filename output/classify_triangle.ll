; ModuleID = "poglin_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"str_fmt_nl" = internal constant [4 x i8] c"%s\0a\00"
@"int_fmt_nl" = internal constant [4 x i8] c"%d\0a\00"
@"read_int_fmt" = internal constant [3 x i8] c"%d\00"
@"read_str_fmt" = internal constant [3 x i8] c"%s\00"
@"temp_str_buffer" = internal global [256 x i8] c"\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00"
define i32 @"main"()
{
entry:
  %"var_a" = alloca i32
  %"var_b" = alloca i32
  %"var_c" = alloca i32
L0:
  store i32 3, i32* %"var_a"
  store i32 4, i32* %"var_b"
  store i32 5, i32* %"var_c"
L1:
  %".5" = getelementptr [46 x i8], [46 x i8]* @"str_const_5664132470441274204", i32 0, i32 0
  %".6" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".5")
L2:
  %"a_val" = load i32, i32* %"var_a"
  %"b_val" = load i32, i32* %"var_b"
  %"_t3" = add i32 %"a_val", %"b_val"
  %"a_val.1" = load i32, i32* %"var_a"
  %"c_val" = load i32, i32* %"var_c"
  %"_t5" = add i32 %"a_val.1", %"c_val"
L4:
L7:
  %".8" = getelementptr [29 x i8], [29 x i8]* @"str_const_767149402951044450", i32 0, i32 0
  %".9" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".8")
L8:
L10:
  %".11" = getelementptr [28 x i8], [28 x i8]* @"str_const_502167877691937837", i32 0, i32 0
  %".12" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %".11")
L11:
  %".14" = getelementptr [27 x i8], [27 x i8]* @"str_const_4512673138535279496", i32 0, i32 0
  %".15" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i8* %".14")
L12:
L9:
L5:
  %".17" = getelementptr [44 x i8], [44 x i8]* @"str_const_3183920170682927672", i32 0, i32 0
  %".18" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18", i8* %".17")
L6:
L3:
  ret i32 0
}

@"str_const_5664132470441274204" = private constant [46 x i8] c"Medidas invalidas: Lados devem ser positivos.\00"
@"str_const_767149402951044450" = private constant [29 x i8] c"Triangulo equilatero valido.\00"
@"str_const_502167877691937837" = private constant [28 x i8] c"Triangulo isosceles valido.\00"
@"str_const_4512673138535279496" = private constant [27 x i8] c"Triangulo escaleno valido.\00"
@"str_const_3183920170682927672" = private constant [44 x i8] c"Medidas invalidas: Nao formam um triangulo.\00"
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
  %"var_num1" = alloca i32
  %"var_num2" = alloca i32
  %"var_sum" = alloca i32
L0:
  store i32 10, i32* %"var_num1"
  store i32 20, i32* %"var_num2"
  store i32 0, i32* %"var_sum"
  %"num1_val" = load i32, i32* %"var_num1"
  %"num2_val" = load i32, i32* %"var_num2"
  %"_t0" = add i32 %"num1_val", %"num2_val"
  store i32 %"_t0", i32* %"var_sum"
  %".6" = getelementptr [24 x i8], [24 x i8]* @"str_const_8969352413057425862", i32 0, i32 0
  %".7" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %".6")
  %"sum_val" = load i32, i32* %"var_sum"
  %".9" = getelementptr [4 x i8], [4 x i8]* @"int_fmt_nl", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sum_val")
  ret i32 0
}

@"str_const_8969352413057425862" = private constant [24 x i8] c"A soma dos inteiros e: \00"
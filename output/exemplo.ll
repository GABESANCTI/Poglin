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
  %"var_nome" = alloca i8*
  %"var_a" = alloca i32
  %"var_b" = alloca i32
  %"var_soma" = alloca i32
L0:
  %".2" = getelementptr [7 x i8], [7 x i8]* @"str_const_4774949917924357282", i32 0, i32 0
  store i8* %".2", i8** %"var_nome"
  %"nome_val" = load i8*, i8** %"var_nome"
  %".4" = getelementptr [4 x i8], [4 x i8]* @"str_fmt_nl", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %"nome_val")
  store i32 5, i32* %"var_a"
  store i32 3, i32* %"var_b"
  %"a_val" = load i32, i32* %"var_a"
  %"b_val" = load i32, i32* %"var_b"
  %"_t0" = add i32 %"a_val", %"b_val"
  store i32 %"_t0", i32* %"var_soma"
  %"soma_val" = load i32, i32* %"var_soma"
  %".9" = getelementptr [4 x i8], [4 x i8]* @"int_fmt_nl", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"soma_val")
  ret i32 0
}

@"str_const_4774949917924357282" = private constant [7 x i8] c"Poglin\00"
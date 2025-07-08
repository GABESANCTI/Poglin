; ModuleID = "poglin_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

declare i32 @"strcmp"(i8* %".1", i8* %".2")

define i32 @"main"()
{
entry:
  %".2" = getelementptr inbounds [5 x i8], [5 x i8]* @"str_-5147196572407435871", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  ret i32 0
}

@"str_-5147196572407435871" = internal constant [5 x i8] c"pog\0a\00"
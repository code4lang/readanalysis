#!/bin/bash
@echo off
FOR /f "delims=" %%G IN ('C:\Users\bdefe\Desktop\pdf_to_excelanalysis\data') DO (
   setlocal enabledelayedexpansion  
   pushd "%%~dpG"
   SET fname=%%~nxG
   SET fname=!fname: =!
   rename "%%~nxG" "!fname!"
   popd
   endlocal
)
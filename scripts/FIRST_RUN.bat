@echo off
REM =============================================================================
REM IRON Framework - FIRST RUN Validation Script
REM =============================================================================
REM Purpose: Run initial empirical validation, collect benchmarks, generate reports
REM Usage:   scripts\FIRST_RUN.bat
REM =============================================================================

setlocal EnableDelayedExpansion

echo.
echo ================================================================================
echo   IRON Framework - First Run Validation
echo ================================================================================
echo.
echo This script will:
echo   [1] Run initial validation suite
echo   [2] Collect benchmarks with multiple runs for stability
echo   [3] Generate analysis reports and charts
echo   [4] Show clear success/failure status
echo.
echo Started: %DATE% %TIME%
echo.
echo ================================================================================

REM Set up paths
set SCRIPT_DIR=%~dp0
set PROJECT_DIR=%SCRIPT_DIR%..
set RESULTS_DIR=%PROJECT_DIR%\iron\benchmarks\results

REM Ensure results directory exists
if not exist "%RESULTS_DIR%" mkdir "%RESULTS_DIR%"

REM =============================================================================
REM STEP 1: Run Initial Validation
REM =============================================================================
echo.
echo [STEP 1/4] Running Initial Validation Suite
echo -------------------------------------------

cd /d "%PROJECT_DIR%"
python -m iron.benchmarks.validate --iterations 50 --warmup 10 --generate-charts

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARNING] Validation completed with warnings or errors
    echo Check the results in: %RESULTS_DIR%
) else (
    echo [OK] Validation completed successfully
)

REM =============================================================================
REM STEP 2: Collect Multiple Benchmark Runs
REM =============================================================================
echo.
echo [STEP 2/4] Collecting Multiple Benchmark Runs (5 iterations)
echo ------------------------------------------------------------

python scripts\collect_benchmarks.py --runs 5 --delay 3 --verbose

if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Benchmark collection completed with warnings
) else (
    echo [OK] Benchmark collection completed successfully
)

REM =============================================================================
REM STEP 3: Generate Analysis Reports and Charts
REM =============================================================================
echo.
echo [STEP 3/4] Generating Analysis Reports and Charts
echo ------------------------------------------------

python scripts\analyze_results.py --charts all --report full

if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Analysis completed with warnings
) else (
    echo [OK] Analysis and chart generation completed successfully
)

REM =============================================================================
REM STEP 4: Verify Targets and Show Summary
REM =============================================================================
echo.
echo [STEP 4/4] Verifying Against Performance Targets
echo ------------------------------------------------

python -m iron.benchmarks.verify verify-targets "%RESULTS_DIR%\validation_latest.json" --target-type windows_npu

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ATTENTION] Some targets were not met - this is expected for CPU baseline
)

REM =============================================================================
REM FINAL SUMMARY
REM =============================================================================
echo.
echo ================================================================================
echo   FIRST RUN COMPLETE
echo ================================================================================
echo.
echo Results Location: %RESULTS_DIR%
echo.
echo Key Files Generated:
echo   - validation_latest.json     : Latest validation results
echo   - validation_latest.md       : Human-readable summary
echo   - benchmark_*.json           : Individual benchmark runs
echo   - analysis_*.md              : Detailed analysis report
echo   - charts\*.png               : Visualization charts
echo.
echo Next Steps:
echo   1. Review validation_latest.md for results summary
echo   2. Check charts\ directory for visualizations
echo   3. Run scripts\PHASE3_KICKOFF.bat to begin Phase 3 implementation
echo.
echo Completed: %DATE% %TIME%
echo ================================================================================
echo.

endlocal
exit /b 0

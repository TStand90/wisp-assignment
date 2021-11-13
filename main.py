from fastapi import FastAPI, HTTPException

from special_math import special_math, special_math_without_recursion

app = FastAPI()


@app.get("/special-math/{number}")
async def get_special_math(number: int):
    try:
        special_math_number = special_math(number)
    except RecursionError:
        raise HTTPException(
            status_code=400,
            detail=f"That number is too large for this endpoint. Try /special-math/{number}/no-recursion"
        )

    return special_math_number


@app.get("/special-math/{number}/no-recursion")
async def get_special_math_without_recursion(number: int):
    return special_math_without_recursion(number)

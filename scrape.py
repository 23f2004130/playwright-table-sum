import asyncio
from playwright.async_api import async_playwright

SEEDS = range(26, 36)

async def main():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in SEEDS:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            await page.goto(url)
            await page.wait_for_selector("table")

            numbers = await page.eval_on_selector_all(
                "table td",
                "cells => cells.map(td => parseFloat(td.innerText)).filter(n => !isNaN(n))"
            )

            total_sum += sum(numbers)

        await browser.close()

    print("FINAL_TOTAL =", total_sum)

asyncio.run(main())

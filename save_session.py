from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="C:\\Users\\Jooao\\playwright-profile",
        channel="chrome",
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://www.mercadolibre.cl")

    print("👉 Inicia sesión manualmente y resuelve captcha")
    input("👉 Presiona ENTER cuando ya estés logueado...")

    # 🔥 AQUÍ guardas la sesión
    context.storage_state(path="state.json")

    context.close()
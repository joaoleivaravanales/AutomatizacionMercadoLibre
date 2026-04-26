from playwright.sync_api import Page, expect

class BuscarPage:

    def __init__(self, page: Page):
        self.page = page
        # En la clase BuscarPage, ya tienes definidos los métodos y localizadores principales para buscar productos y seleccionar el primer resultado, que cubren los pasos del feature de búsqueda de iPhone y sus escenarios:
        #  - open_home: para abrir la página principal (Given)
        #  - buscar_producto: para buscar un producto (When)
        #  - seleccionar_primer_producto: para presionar en el primer resultado (When)
        #  - validar_resultados: para verificar que aparecen resultados (puede usarse como paso de validación intermedio si lo necesitas)
        #
        # Lo que podría faltar es un método para verificar el título del producto, como lo pide el step:
        # 'Then Verifico que el titulo del producto sea "<titulo>"'
        
        def verificar_titulo_producto(self, titulo: str):
            # Suponiendo que el título del producto está en un elemento h1 o con un selector específico en la página de detalle
            titulo_selector = self.page.locator('h1')  # Ajusta este selector según el HTML real de la página de producto
            expect(titulo_selector).to_have_text(titulo, timeout=10000)
    

        # LOCATORS 
        self.input_busqueda = page.get_by_placeholder("Buscar productos, marcas y más")
        self.btn_buscar = page.get_by_role("button", name="Buscar")
        self.resultados = self.page.locator(".ui-search-layout__item")
        self.primer_resultado = page.locator(".ui-search-result__content").first

    def open_home(self, base_url):
        self.page.goto(base_url)

    def buscar_producto(self, producto: str):
        self.input_busqueda.fill(producto)
        self.input_busqueda.press("Enter")

    def validar_resultados(self):
            expect(self.resultados.first).to_be_visible(timeout=10000)

    def seleccionar_primer_producto(self):
        self.primer_resultado.click()
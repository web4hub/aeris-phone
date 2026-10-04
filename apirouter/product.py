# products.py
ar = APIRouter()

@ar
def details(pid: int): return f"Here are the product details for ID: {pid}"

@ar
def all_products(req):
    return Div(
        Div(
            Button("Details",hx_get=details.to(pid=42),hx_target="#products_list",hx_swap="outerHTML",),
        ), id="products_list")

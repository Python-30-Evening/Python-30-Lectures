var json_teapot = '{"title": "Teapot ARG", "price": 1500, "in_stock": true, "description": "cool teapot"}'
var js_teapot = JSON.parse(json_teapot)


document.getElementById('title').innerText = js_teapot.title
document.getElementById('price').innerText = js_teapot.price
document.getElementById('in_stock').innerText = js_teapot.in_stock
document.getElementById('desc').innerText = js_teapot.description

from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Libros, Categorias, PedidoXCliente, LibroXAutor, Autores
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


def principal(request):
    libros =  Libros.objects.all()
    pedidos =  PedidoXCliente.objects.all()
    clientes = Clientes.objects.all()
    autores = Autores.objects.all()
    categorias = Categorias.objects.all()
    return render(request, "appngvdj/index.html", {"libros": libros, "autores": autores, "clientes": clientes, "categorias": categorias, "pedidos": pedidos})


def agregarClientes(request):
    if request.method == 'GET':
        return render(request, "appngvdj/clientes.html")  
    elif request.method == 'POST':
        nombres =  request.POST.get('nombres')
        apellidos =  request.POST.get('apellidos')
        identificacion =  request.POST.get('id')
        telefono =  request.POST.get('telefono')
        direccion =  request.POST.get('direccion')
        correo =  request.POST.get('correo')
        
        cliente = Clientes(
            nombres=nombres,
            apellidos=apellidos,
            identificacion=identificacion,
            telefono = telefono,
            direccion = direccion,
            correo = correo
        )
        cliente.save()
        return redirect('index')
    
    
def agregarLibro(request):
    categorias = Categorias.objects.all()
    if request.method == 'GET':
        return render(request, 'appngvdj/libros.html', { 'categorias' : categorias })
    elif request.method ==  'POST':
        isbn = request.POST.get('isbn')
        titulo = request.POST.get('titulo')
        fecha_pub = request.POST.get("fecha_pub")
        precio = request.POST.get("precio")
        categoria_nombre = request.POST.get('categoria')
        categoria = Categorias.objects.get(categoria=categoria_nombre)
        canStock = request.POST.get('stock')
        libro = Libros(
            isbn=isbn,
            titulo=titulo,
            fecha_pub=fecha_pub,
            precio=precio,
            id_categoria=categoria,  # Aquí pasamos el objeto de categoría, no el queryset
            cantidad_stock=canStock
        )
        libro.save()
        return redirect('index')

    

def agregarPedido(request):
    if request.method == "POST":
        idUsuario = request.POST.get("identificacion")
        libro = request.POST.get("libro")
        cantidad = request.POST.get("cantidad")
        cantidad = int(cantidad)
        
        try:
            libreria = Libros.objects.get(titulo = libro)
            usuario = Clientes.objects.get(identificacion = idUsuario) 
        except ObjectDoesNotExist:
            return redirect("index")
        
        if libreria.cantidad_stock - cantidad< 0:
            return redirect("index")
        else:
            pedido = PedidoXCliente(
                id_cliente = usuario,
                isbn = libreria,
                cantidad = cantidad,
                fecha_ped = timezone.now()
            )
            
            libreria.cantidad_stock -= cantidad
            libreria.save()
            pedido.save()
            
            return redirect("index")
    return render(request, "appngvdj/agregar.html", )


def modificarAutor(request, id_autor):
    autor = Autores.objects.get(id_autor = id_autor)
    if request.method=="GET":
        return render(request, 'appngvdj/editarAutor.html', {"autor": autor})
    elif request.method =="POST":
        autor.nombres = request.POST.get('nombres')
        autor.apellidos = request.POST.get('apellidos')
        autor.save()
        return redirect('index')


def modificarCliente(request, idCliente):
    cliente = Clientes.objects.get(id_cliente = idCliente)
    if request.method == 'GET':
        return render(request, 'appngvdj/editarCliente.html', {"cliente" : cliente})
    elif request.method == 'POST':
        cliente.nombres = request.POST.get( "nombres" )
        cliente.apellidos = request.POST.get( "apellidos" )
        cliente.identificacion = request.POST.get( "id" )
        cliente.telefono = request.POST.get( "telefono" )
        cliente.direccion = request.POST.get( "direccion" )
        cliente.correo = request.POST.get( "correo" )
        cliente.save()
        return redirect('index')


def agregarAutor (request):
    librosSinAutor = []
    libros = Libros.objects.all()
    for libro in libros:
        if not LibroXAutor.objects.filter(isbn=libro.isbn).exists():
            librosSinAutor.append(libro)
    if request.method == 'GET':
        return render(request, 'appngvdj/autores.html', { 'libros' : librosSinAutor })
    elif request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        libro_titulo = request.POST.get('libro')

        autor = Autores.objects.create(nombres=nombres, apellidos=apellidos)

        if libro_titulo:
            libro = Libros.objects.get(titulo=libro_titulo)
            LibroXAutor.objects.create(isbn=libro, id_autor=autor)

        return redirect('index')


def modificarLibro (request, isbn):
    libro = Libros.objects.get(isbn=isbn)
    categorias = Categorias.objects.all()
    if request.method == 'GET':
        return render(request, 'appngvdj/editarLibro.html', {'libro' : libro, 'categorias' : categorias })
    elif request.method == 'POST':
        titulo = request.POST.get( "titulo" )
        fecha_pub = request.POST.get( "fecha_pub")
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria = Categorias.objects.filter(categoria = request.POST.get('categoria')).first() 
        
        fecha = fecha_pub
        
        libro.titulo = titulo
        libro.fecha_pub=fecha
        libro.precio=precio
        libro.cantidad_stock = stock
        libro.id_categoria=categoria
        libro.save()
        return redirect('index')
    

def modificarPedido(request, idPedido):
    pedido = PedidoXCliente.objects.get(id_pedido=idPedido)
    libreria = Libros.objects.get(titulo = pedido.isbn.titulo)
    if request.method == "POST":
        nuevaCant = request.POST.get("nuevaCantidad")
        nuevaCant = int(nuevaCant)
        if nuevaCant: 
            libreria.cantidad_stock += pedido.cantidad - nuevaCant
            libreria.save()
            pedido.cantidad = nuevaCant
            pedido.save()
            return redirect("pedidos")
    return render(request, "appngvdj/editarPedido.html", {"pedido": pedido})

def eliminarPedido(request, idPedido):
    pedido = get_object_or_404(PedidoXCliente, id_pedido=idPedido)
    libreria = Libros.objects.get(titulo = pedido.isbn.titulo)
    
    if request.method == 'POST':
        libreria.cantidad_stock += pedido.cantidad
        libreria.save()
        pedido.delete()
        return redirect('pedidos')
    
    return render(request, 'appngvdj/eliminarPedido.html', {'pedido': pedido})


def visualizarPedidos(request):
    if request.method == "POST":
        identificacion = request.POST.get("identificacion")
        cliente = Clientes.objects.filter(identificacion=identificacion).first()
        if cliente:
            pedidos = PedidoXCliente.objects.filter(id_cliente=cliente.id_cliente)
            return render(request, "appngvdj/misPedidos.html", {"cliente": cliente, "pedidos": pedidos})
        else:
            return redirect('pedidos')
    return render(request, "appngvdj/misPedidos.html")
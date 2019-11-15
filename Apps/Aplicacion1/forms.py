from django import forms
from .models import inventario,empleado,venta,detallefactura
from django.forms import ModelForm

class inventarioForm(ModelForm):

	class Meta:
		model = inventario

		fields = [
				'codigo_inventario',
				'nombre_inventario',
				'marca_invetario',
				'existencia_inventario',
				'precio_inventario',
		]
		labels = {

				'codigo_inventario': 'codigo del inventario',
				'nombre_inventario': 'nombre del producto',
				'marca_invetario': 'marca del producto',
				'existencia_inventario': 'existencia del producto',
				'precio_inventario': 'precio unitario',
		}
		widgets = {

				'codigo_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'nombre_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'marca_invetario': forms.TextInput(attrs={'class':'form-control'}),
				'existencia_inventario': forms.TextInput(attrs={'class':'form-control'}),
				'precio_inventario' : forms.TextInput(attrs={'class':'form-control'}),
		}


class empleadoForm(ModelForm):

	class Meta:
		model = empleado
		fields = [
				'codigo_empleado',
				'nombre_empleado',
				'email_empleado',
				'fecha_empleado',

		]
		labels = {
				'codigo_empleado': 'codigo del empleado',
				'nombre_empleado': 'nombre del empleado',
				'email_empleado': 'E-mail',
				'fecha_empleado': 'fecha de inicio',
		
		}
		widgets = {
				  'codigo_empleado': forms.TextInput(attrs={'class':'form-control'}),
				  'nombre_empleado': forms.TextInput(attrs={'class': 'form-control'}),
				  'email_empleado': forms.TextInput(attrs={'class': 'form-control'}),
				  'fecha_empleado': forms.SelectDateWidget(years=range(2019,2050)),


		}


class ventaForm(ModelForm):

	class Meta:
		model = venta
		fields =[
				'codigo_empleado',
				'codigo_venta',
				'fecha_venta',
				'total_venta',
		]
		labels= {
				'codigo_empleado': 'codigo del empleado',
				'codigo_venta': 'codigo de venta',
				'fecha_venta': 'fecha de venta',
				'total_venta': 'total de la venta',

		}
		widgets = {
				  'codigo_empleado': forms.Select(attrs={'class':'form-control'}),
				  'codigo_venta': forms.TextInput(attrs={'class': 'form-control'}),
				  'fecha_venta': forms.SelectDateWidget(years=range(2019,2050)),
				  'total_venta': forms.TextInput(attrs={'class': 'form-control'}),
		}
class detallefacturaForm(ModelForm):

	class Meta:
		model = detallefactura
		fields = [
				'codigo_venta',
				'codigo_inventario',
				'cantidad_producto',
				'Precio_unitario',
				'precio_total',
				'fecha_detalle',
		]
		labels ={
				'codigo_venta': 'empleado',
				'codigo_inventario': 'codigo de venta',
				'cantidad_producto': 'cantidad',
				'Precio_unitario': 'precio del producto',
				'precio_total': 'total',
				'fecha_detalle': 'fecha',

		}
		widgets = {
			'codigo_inventario': forms.Select(attrs={'id':'idproducto'}),
			 'fecha_detalle': forms.SelectDateWidget(years=range(2019,2050)),
		}

	def __init__(self, *args, **kwargs):
		super(detallefacturaForm, self).__init__(*args, **kwargs)
		#self.fields['codigo_inventario'].widget.attrs\
        #    .update({
        #        'id': 'codigo'
        #    })
		self.fields['Precio_unitario'].widget.attrs\
            .update({
                'id': 'precio'
            })
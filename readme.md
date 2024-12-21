# Plantilla Personalizada de Documentos Odoo

Este repositorio contiene una plantilla personalizada de documentos para Odoo, diseñada para extender y personalizar el diseño de documentos como facturas, cotizaciones y otros informes. Aprovecha la plantilla `web.external_layout_striped`, modificándola para incluir logotipos de empresas, códigos QR y detalles dinámicos de documentos según el contexto (factura, detalles del socio, etc.).

## Características

- **Encabezado Personalizado**: Muestra el logotipo de la empresa, los detalles de la empresa y un código QR dinámico.
- **Información Dinámica de Documentos**: Muestra tipos de operación, valor TRM y otros detalles relevantes del documento.
- **Detalles del Socio**: Muestra el NIT, nombre, dirección, teléfono y correo electrónico del socio.
- **Detalles de Facturas y Cotizaciones**: Incluye datos como número de documento, información del vendedor, términos de pago, etc.
- **Fondo y Estilo**: Fondos personalizables y estilos para cada empresa.
- **Diseño Flexible**: Soporta varias secciones dinámicas como los detalles de la empresa, las líneas de la factura y el pie de página.

## Requisitos Previos

- **Odoo.sh**: Esta plantilla está diseñada para funcionar en un entorno Odoo.sh.
- **Odoo 17+**: Asegúrate de estar utilizando la versión de Odoo 17 o superior.
- **Acceso de Administrador**: Necesitarás acceso de administrador para instalar la plantilla personalizada en tu instancia de Odoo.

## Guía de Instalación

Sigue estos pasos para instalar la plantilla personalizada de documentos en Odoo.sh:

### 1. Clonar el Repositorio

Clona este repositorio en tu proyecto de Odoo.sh.

1. Abre tu proyecto de Odoo.sh.
2. Ve a la pestaña **Git**.
3. Haz clic en **Clonar un repositorio** y pega la URL del repositorio para clonar el proyecto.

### 2. Instalar aplicacion

Una vez que la plantilla personalizada se haya agregado a tu entorno Odoo.sh, instala la aplicacion.

### 3. Probar la Plantilla

Para asegurarte de que la plantilla esté funcionando correctamente:
1. Abre cualquier factura o cotización.
2. Verifica que aparezca el diseño personalizado, con el logotipo de la empresa, el código QR y los detalles dinámicos del documento.
3. Prueba diferentes tipos de documentos (por ejemplo, facturas, cotizaciones) para asegurarte de que todas las secciones se muestren correctamente.

## Personalización

Puedes personalizar la plantilla modificando lo siguiente:

- **Logotipo y Detalles de la Empresa**: Actualiza el logotipo de la empresa y la información adicional en la sección del encabezado de la plantilla.
- **Código QR**: Si necesitas ajustar la lógica del código QR o los datos que muestra, modifica la etiqueta `<img>` asociada con `o.ei_qr_image`.
- **Campos Dinámicos**: Agrega o elimina campos en las secciones del documento, como números de factura, detalles del socio o valores de impuestos.
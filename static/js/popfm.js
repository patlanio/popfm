var estaReproduciento = false;
var estacionActual;
var totalSlides;
var slideActual = 0;
var intervalo;

/*

Esta libreria tiene como dependencia Jquery 1.9
para poder usarla hay que tener definidos en nuestro HTML los elementos que se describen en el codigo con la siguiente estructura

$('#OBJETOS_POR_ID')...
$('.OBJETOS_POR_CLASE')...

*/
//cuando la pagina esta lista se ejecuta la funcion main
$(document).on('ready', main);
function main(){
	//obtenemos la url de la fuente del audio que se esta transmitiendo por internet totalmente en vivo
	estacionActual = document.getElementById('fuente');
	//se agrega el evento para pausar/iniciar el audio
	$('.boton-play').on('click', iniciarPausarRadio);
	//se agrega el evento para mostrar un formulario para enviar saludos y dedicatorias
	$('.saludar').on('click', mostrarOcultarFormulario);
	//se agrega el evento para cerrar el formulario anterior
	$('.cerrar').on('click', mostrarOcultarFormulario);
	//$('boton-play').click();

	/*
	Si estamos en la pagina principal checa que haya elementos "portada"
	y cuenta cuantos son, en caso de que sean menos de 2 se ocultan las flechas de navegacion
	si no, se agregan eventos para mover las portadas hacia la derecha o izquierda
	*/
	if ($('.portadas .portada').size() < 2 ) {
		//alert("Son poquitas, no se iniciara el slider");
		$('.flecha').hide();
	}else{
		intervalo = setInterval('desplazarSlider(1)', 5000);
		$('.flecha-izquierda').on('click', function(){
			desplazarSlider(-1);
		});
		$('.flecha-derecha').on('click', function(){
			desplazarSlider(1);
		});
		//$(".bolitas").mouseenter(function(){intervalo = clearInterval(intervalo);
		//}).mouseleave(function(){intervalo = setInterval('desplazarSlider()', 5000);});
		/*
		*CON ESTO REORGANIZAMOS LO QUE EL CSS PURO TIENE
		*EL PURO CSS FUNCIONA CON 3 DIAPOSITIVAS MAXIMO (POR DEFAULT)
		*/
		totalSlides = $('.portadas .portada').size();
		$('.slider').css('width', (totalSlides*100)+"%");
		$('.slide').css('width', (100 / totalSlides )+"%");
	}
	sumarAnchoSaludos();
}

/*
Esto es para mover los saludos de forma tal que se muestren todos por la pantalla
*/
function sumarAnchoSaludos(){
	//alert($('.saludos').width());
	var suma = 0;
	$('.saludo').each(function(indice, elemento) {
		suma += $(elemento).width();
	});
	recorrerSaludos();
	//$('.saludo:first-child').css('animation-duration', Math.round(suma / PPS )+'s');
	//alert("La suma de los saludos es: "+suma);
	//alert("Los segundos son: "+ $('.saludo:first-child').css('animation-duration'));
}

function recorrerSaludos(){
	var PPS = 32; //PIXELES POR SEGUNDO
	var ancho = $('.saludo:first-child').width() * 1.25;
	//var pad = $('.saludo:first-child').css('padding-left');
	//alert(ancho);
	var t = (ancho / PPS)*1000;
	$(".saludo:first-child").animate({
		marginLeft: (-ancho + 14 +'px')
	}, t, function() {
	//}, t, "linear", function() {
		$('.saludos').append(this);
		$(this).css("margin", "0px")
		recorrerSaludos();
	});
}

//Funcion para mostrar/ocultar formularios
function mostrarOcultarFormulario(){
	$('.formulario-saludo').fadeToggle('fast');
}
//funcion para mover las portadas 
function desplazarSlider(direccion){
	if (slideActual == totalSlides-1) {slideActual = 0;}
	else{slideActual++}
	$(".slider").animate({
		marginLeft: (-100 *direccion * slideActual + "%")
		}, 700);
	//slideActual++;
}

//funcion para iniciar/pausar audios
function iniciarPausarRadio(){
	if (!estaReproduciento) {
		estacionActual.play();
		estaReproduciento = true;
		//var h = document.getElementById('lista-letras').classList.toggle('colapsado');
	}else{
		estacionActual.pause();
		estaReproduciento = false;
	}
	$(this).toggleClass('fa-pause');
	$(this).toggleClass('parpadeando');
}
$(function(){
            $("#mi-formulario").validate({

                rules:{
                    nom:{
                        required:true
                    },
                    correo:{
                        required:true,
                        email:true
                    },
                    fono:{
                        required:true
                    },
                    pass:{
                        required:true
                    },
                    fecha:{
                        required:true
                    },
                    pass2:{
                        required:true,
                        equalTo:pass
                    },
                },//rules
                messages:{
                    nom:{
                        required:'Ingrese nombre de usuario',
                        minlength:'Caracteres insuficientes'
                    },
                    email:{
                        required:'Ingrese correo electronico',
                        email:'Formato de correo invalid'
                    },
                    fono:{
                        required:'Ingrese telefono',
                        minlength:'Digitos insuficientes'
                    },
                    fecha:{
                        required:'Ingrese una fecha',
                        minlength:'Seleccione una fecha valida'
                    },
                    pass:{
                        required:'Ingrese una contraseña',
                        minlength:'Caracteres insuficientes'
                    },
                    pass2:{
                        required:'Reingrese contraseña',
                        minlength:'Caracteres insuficientes',
                        equalTo:'Contraseñas no coinciden'
                    }
                }
            })
        });
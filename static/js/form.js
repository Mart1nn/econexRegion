
// $('#anchor_form').validate({
// 	rules: {
// 		user_name: {
// 			required: true,
// 			user_name: true
// 		},
// 		user_phone: {
// 			required: true
// 		}
//     }

// });

// user_phone
// user_email

// $(document).ready(function() {
//     $("#signupForm").validate({
//         rules: {
//             profileAddress: "required",
//             profilePostcode: "required",
//             profileGemeente: "required",
//             profielMobiel: "required",
//             profileNoodnr: "required",
//             profileLogin: {
//                 required: true,
//                 email: true
//             },
//             profileNewPassword: {
//                 minlength: 6
//             },
//             profileNewPasswordRepeat: {
//                 minlength: 6,
//                 equalTo: "#profileNewPassword"
//             }
//         },
//         messages: {
//             profileAddress: "Dit is een verplicht item",
//             profilePostcode: "Dit is een verplicht item",
//             profileGemeente: "Dit is een verplicht item",
//             profielMobiel: "Dit is een verplicht item",
//             profileNoodnr: "Dit is een verplicht item",
//             profileLogin: {
//                 required: "Gelieve een geldig e-mailadres in te geven",
//                 email: "Gelieve een geldig e-mailadres in te geven"
//             },
//             profileNewPassword: {
//                 minlength: "Het nieuwe paswoord moet mininum 6 tekens lang zijn"
//             },
//             profileNewPasswordRepeat: {
//                 minlength: "Het nieuwe paswoord moet mininum 6 tekens lang zijn",
//                 equalTo: "Gelieve hetzelfde paswoord als hierboven in te geven"
//             }
//         },
//         errorElement: "em",
//         errorPlacement: function ( error, element ) {
//             // Add the `help-block` class to the error element
//             error.addClass( "help-block" );

//             if ( element.prop( "type" ) === "checkbox" ) {
//                 error.insertAfter( element.parent( "label" ) );
//             } else {
//                 error.insertAfter( element );
//             }
//         },
//         highlight: function ( element, errorClass, validClass ) {
//             $( element ).parents( ".col-sm-5" ).addClass( "has-error" ).removeClass( "has-success" );
//         },
//         unhighlight: function (element, errorClass, validClass) {
//             $( element ).parents( ".col-sm-5" ).addClass( "has-success" ).removeClass( "has-error" );
//         }
//     } );


// });
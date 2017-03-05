/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Inicial;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author Paola
 */
public class Prueba {

    

    public static OkHttpClient webClient = new OkHttpClient();
    
    public String Insertar(String correo) {
        String [] parametros = correo.split("@");
        String letra = parametros[0];
        char etra = letra.charAt(0);
        letra = etra + "";
        RequestBody formBody = new FormEncodingBuilder()
                .add("letra", letra)
                .add("dominio", parametros[1])
                .add("nombre",parametros[0])
                .build();
        String r = getString("insertar", formBody); 
        System.out.println(r + "---");
        String r1 = getString("e", formBody); 
        System.out.println(r1 + "---");
        return r;
    }
    
    public String Eliminar(String correo) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", correo)
                .add("dato2", "4")
                .build();
        String r = getString("eliminar", formBody); 
        return r;
    }
    
    public String prueba(){
        String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("metodoWeb", formBody); 
        return r;
    }
            
    
    public void BuscarLetra(String letra) {
        
        char etra = letra.charAt(0);
        letra = etra + "";
        RequestBody formBody = new FormEncodingBuilder()
                .add("letra", letra)
                .build();
        String r = getString("BuscarLetra", formBody); 
        System.out.println(r + "---");
        String r1 = getString("e", formBody); 
        System.out.println(r1 + "---");
    }
    
    public void BuscarDominio(String dominio) {
      
        RequestBody formBody = new FormEncodingBuilder()
                .add("dominio", dominio)

                .build();
        String r = getString("BuscarDominio", formBody); 
        System.out.println(r + "---");
        String r1 = getString("e", formBody); 
        System.out.println(r1 + "---");
    }
 
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Prueba.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Prueba.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}

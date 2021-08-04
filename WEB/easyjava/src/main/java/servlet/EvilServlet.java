package servlet;

import sun.misc.BASE64Decoder;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import security.SafeObjectInputStream;

@WebServlet(
        name = "EvilServlet",
        urlPatterns = {"/evil"}
)
public class EvilServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        ServletOutputStream out = resp.getOutputStream();
        try{

            String unser = req.getParameter("p");
            final BASE64Decoder decoder = new BASE64Decoder();
            byte[] res =  decoder.decodeBuffer(unser);
            ObjectInputStream ois = new SafeObjectInputStream(new ByteArrayInputStream(res));
            Object o = ois.readObject();
        }
        catch (Exception e){
            System.out.println(e);
        }
        out.write("please give me a param p".getBytes());
        out.flush();
        out.close();
    }
    protected void testUns() throws Exception{

    }

}

package security;


import java.io.*;


public class SafeObjectInputStream extends ObjectInputStream {



    public SafeObjectInputStream(InputStream inputStream) throws IOException {
        super(inputStream);
    }


    @Override
    protected Class<?> resolveClass(final ObjectStreamClass desc)
            throws IOException, ClassNotFoundException
    {
        String className = desc.getName();

    

        String[] denyClasses = {"java.net.InetAddress",
                                "org.apache.commons.collections.Transformer",
                                "org.apache.commons.collections.functors",
                                "java.util.LinkedHashSet",
                                "java.rmi.",
                                "sun.rmi."
                            };

        for (String denyClass : denyClasses) {
            if (className.startsWith(denyClass)) {
                throw new InvalidClassException("Unauthorized deserialization attempt", className);
            }
        }

        return super.resolveClass(desc);
    }



}

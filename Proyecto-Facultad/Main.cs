using Proyecto_Facultad;
using System.Net;
using static System.Runtime.InteropServices.JavaScript.JSType;


Empresa empresaTelefonica = new Empresa();

int opc;

string menu = "1: Agregar una nueva linea a un cliente " +
    "\n2: Eliminar una linea a un cliente " +
    "\n3: Realizar una llamada (desde una linea)" +
    "\n4: Enviar un mensaje (desde una linea)" +
    "\n5: Recargar saldo a una linea " +
    "\n6: Suspender o reactivar una linea " +
    "\n7: Transferir saldo entre 2 lineas " +
    "\n8: Listar todas las lineas de un cliente" +
    "\n9: Listar todos los clientes y sus lineas " +
    "\n0: Salir\n";
    
Console.WriteLine("Bienvenido al menu de gestiones de la empresa");

try
{
    Console.WriteLine("\n" + menu);
    Console.Write("Elige una opción del menu: ");
    opc = int.Parse(Console.ReadLine());

    while (opc != 0)
    {
        try
        {
            switch (opc)
            {

                case 1:
                    try
                    {
                        Console.Write("Ingresa el dni del cliente: ");
                        int dni = int.Parse(Console.ReadLine());

                        Console.Write("Ingresa el numero del cliente: ");
                        int numero = int.Parse(Console.ReadLine());

                        Console.WriteLine("Que plan desea contratar: \n");

                        string menu2 = "1. Plan Basico" +
                            "\n2. Plan Medio" +
                            "\n3. Plan Alto";

                        Console.WriteLine(menu2);

                        int opcion = int.Parse(Console.ReadLine());
                        string plan;
                        while (opcion != 1 && opcion != 2 && opcion != 3)
                        {
                            Console.Write("\nOpción no válida. Vuelva a intentarlo: ");
                            Console.WriteLine(menu2);
                            opcion = int.Parse(Console.ReadLine());
                        }

                        if (opcion == 1)
                        {
                            plan = "Plan Basico";
                            empresaTelefonica.AgregarLineaACliente(dni, numero, plan);
                        }

                        else if (opcion == 2)
                        {
                            plan = "Plan Medio";
                            empresaTelefonica.AgregarLineaACliente(dni, numero, plan);
                        }

                        else if (opcion == 3)
                        {
                            plan = "Plan Alto";
                            empresaTelefonica.AgregarLineaACliente(dni, numero, plan);
                        }

                        else
                        {
                            Console.WriteLine("la opcion ingresada no es valida.");
                        }

                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error mientras se pedian los datos: " + ex.Message);
                    }

                    break;


                case 2:

                    try
                    {
                        Console.Write("Ingresa el dni del cliente: ");
                        int dni = int.Parse(Console.ReadLine());

                        Console.Write("Ingresa el numero del cliente: ");
                        int numero = int.Parse(Console.ReadLine());

                        empresaTelefonica.EliminarLineaACliente(numero, dni);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }
                    break;

                case 3:

                    try
                    {
                        Console.Write("Ingresa el numero: ");
                        int numero = int.Parse(Console.ReadLine());

                        Linea linea = empresaTelefonica.BuscarLinea(numero);

                        if(linea != null)
                        {
                            linea.RealizarLlamado();
                        }
                        
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }

                    break;

                case 4:

                    try
                    {
                        Console.Write("Ingresa el numero: ");
                        int numero = int.Parse(Console.ReadLine());

                        Linea linea = empresaTelefonica.BuscarLinea(numero);

                        if(linea != null)// Agregamos este if aca porque si linea es null tira un error
                        {
                            linea.EnviarMensaje();
                        }
                        
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }

                    break;

                case 5:

                    try
                    {
                        Console.Write("Ingresa el numero a recargar saldo: ");
                        int numero = int.Parse(Console.ReadLine());

                        Linea linea = empresaTelefonica.BuscarLinea(numero);

                        if (linea != null)
                        {
                            Console.Write("Ingresa el monto a cargar: ");
                            double monto = double.Parse(Console.ReadLine());
                            linea.RecargarSaldo(monto);
                        }
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }


                    break;

                case 6:
                    try
                    {
                        Console.Write("Ingresa el numero a activar o desactivar: ");
                        int numero = int.Parse(Console.ReadLine());

                        Linea linea = empresaTelefonica.BuscarLinea(numero);

                        if (linea != null) //Agregamos este if aca porque si no existe la linea, tira un error
                        {
                            linea.SuspenderReactivarLinea();
                        }
                        

                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }

                    break;

                case 7:

                    try
                    {
                        Console.Write("Ingresa el numero de origen: ");
                        int numeroOrigen = int.Parse(Console.ReadLine());

                        Console.Write("Ingresa el numero de destino: ");
                        int numeroDestino = int.Parse(Console.ReadLine());

                        Console.Write("Ingresa el monto a transferir: ");
                        double saldo = double.Parse(Console.ReadLine());

                        empresaTelefonica.TransferirSaldo(numeroOrigen, numeroDestino, saldo);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }
                    break;

                case 8:
                    try
                    {
                        Console.Write("Ingresa el dni del cliente: ");
                        int dni = int.Parse(Console.ReadLine());

                        empresaTelefonica.ListarLineasDeCliente(dni);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }

                    break;

                case 9:

                    try
                    {
                        empresaTelefonica.ListarClientes();
                    }
                    catch (EmpresaSinClientesException ex)
                    {   
                        Console.WriteLine("Ocurrió un error: " + ex.Message);
                    }
                    break;

                default:
                    Console.WriteLine("Opcion ingresada no valida, intentalo nuevamente");
                    break;
            }

            Console.WriteLine("\n" + menu);
            Console.Write("Elige una opción del menu: ");
            opc = int.Parse(Console.ReadLine());

        }
        catch (Exception ex)
        {
            Console.WriteLine("Ocurrió un error: " + ex.Message);
        }

    }

}catch(Exception ex)
{
    Console.WriteLine("Ocurrió un error: " + ex.Message);
}


Console.WriteLine("Saliendo...");

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Proyecto_Facultad
{
    internal class Empresa
    {

        private List<Cliente> clientes = new List<Cliente>();

        public List<Cliente> Clientes
        {
            get{return clientes;}

            set{clientes = value;}
        }

        /*public List<Linea> Lineas
        {
            get{return lineas;}

            set{lineas = value;}
        }*/


        //Metodos ******************

        public void AgregarLineaACliente(int dniCliente, int numeroDeLinea, string planContratado)
        {
            try
            {
               
                Linea lineaExistente = BuscarLinea(numeroDeLinea);

                

                if (lineaExistente != null)
                {
                    Console.WriteLine("\nEl numero de telefono ingresado ya existe en el sistema");
                }
                else
                {
                    Console.WriteLine("Como la linea no existe, se la creará."); //Se cambio de lugar esto para que no se muestre si el numero ya existe
                    Cliente clienteExistente = BuscarCliente(dniCliente);
                    Cliente cliente; // Variable para guardar el cliente (nuevo o existente)

                    if (clienteExistente == null)
                    {
                        Console.WriteLine("Como el cliente no existe, se procedera a crearlo.");
                        cliente = AgregarCliente(dniCliente);
                        clientes.Add(cliente);
                        Console.WriteLine("\nCliente creado y agregado correctamente");
                    }
                    else
                    {
                        
                        cliente = clienteExistente;
                    }

                    
                    Linea linea = new Linea(numeroDeLinea, planContratado, dniCliente);
                    cliente.Lineas.Add(linea); 

                    Console.WriteLine("\nLinea de telefono agregada correctamente");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al agregar linea a un cliente" + ex.Message);
            }
        }

        public void EliminarLineaACliente(int numeroDeLinea, int dniCliente)
        {
            try
            {
                Cliente clienteExistente = BuscarCliente(dniCliente);

                if (clienteExistente == null)
                {
                    Console.WriteLine("\nNo existe ningun cliente con ese DNI");

                }
                else
                {
                    Linea lineaEliminar = null;
                    foreach (Linea l in clienteExistente.Lineas)
                    {
                        if (l.Numero == numeroDeLinea)
                        {
                            lineaEliminar = l;
                        }
                    }

                    if (lineaEliminar != null)
                    {
                        clienteExistente.Lineas.Remove(lineaEliminar); //La linea se borra por fuera del bucle para evitar problemas / errores
                        Console.WriteLine("\nLinea eliminada correctamente");

                        if (clienteExistente.Lineas.Count == 0) //Por que se hace esto? Porque en la consigna dice que si el cliente no tiene ninguna linea se da de baja
                        {
                            clientes.Remove(clienteExistente);
                            Console.WriteLine("\nSe dió de baja al cliente al no tener ninguna linea asignada");
                        }
                    }
                    else
                    {
                        Console.WriteLine("\nNo existe ningun cliente que tenga esa linea");
                    }

                    
                }

            }catch(Exception ex)
            {
                Console.WriteLine("Error al eliminar una linea del cliente: " + ex.Message);
            }
        }

        public void ListarLineasDeCliente(int dniCliente)
        {
            try
            {
                Cliente clienteExistente = BuscarCliente(dniCliente);

                if (clienteExistente != null)
                {
                    Console.WriteLine("\nListamos las lineas del cliente: " + clienteExistente.Nombre);
                    for(int i = 0; i < clienteExistente.Lineas.Count; i++)
                    {
                        Console.WriteLine("\nNumero: {0}, \nPlan: {1}, \nSaldo:{2}, \nEstado:{3}", 
                            clienteExistente.Lineas[i].Numero, clienteExistente.Lineas[i].PlanContratado, clienteExistente.Lineas[i].SaldoDisponible,
                            clienteExistente.Lineas[i].EstadoDeLinea);
                    }
                }


            }catch(Exception ex)
            {
                Console.WriteLine("Hubo un error al listar lineas del cliente: " + ex.Message);
            }
        }

        public void ListarClientes()
        {
            try
            {

                if (clientes != null && clientes.Count > 0) 
                {
                    for (int i = 0; i < clientes.Count; i++)
                    {
                        clientes[i].MostrarDatos();

                        if (clientes[i].Lineas != null)
                        {
                            for (int j = 0; j < clientes[i].Lineas.Count; j++)
                            {
                                Console.WriteLine("\nNumero: {0}, \nPlan: {1}, \nSaldo:{2}, \nEstado:{3}",
                                    clientes[i].Lineas[j].Numero, clientes[i].Lineas[j].PlanContratado, clientes[i].Lineas[j].SaldoDisponible,
                                    clientes[i].Lineas[j].EstadoDeLinea);
                                Console.WriteLine("-------------------------");
                            }
                        }
                        else
                        {
                            Console.WriteLine("\nEl cliente no tiene ninguna linea asignada");
                        }
                        
                    }
                }
                else
                {
                    
                    throw new EmpresaSinClientesException();
                }

                
                
            }catch(EmpresaSinClientesException esce)
            {
                Console.WriteLine("La empresa no cuenta con ningun cliente");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al listar clientes" + ex.Message);
            }
        }


        public Cliente AgregarCliente(int dniCliente) //Este metodo quizás esté de más.
                                                    //Quizás se use para pedir datos del cliente a crear. 
        {
            try
            {
                Console.WriteLine("\nCreación de cliente: ");

                Console.Write("Ingrese el nombre del cliente: ");
                string nombre = Console.ReadLine();

                Console.Write("Ingrese la dirección del cliente: ");
                string direccion = Console.ReadLine();

                Console.Write("Ingrese el telefono alternativo del cliente: ");
                int telAlternativo = int.Parse(Console.ReadLine());

                Console.Write("Ingrese el correo del cliente: ");
                string correo = Console.ReadLine();

                Cliente cliente = new Cliente(nombre, dniCliente, direccion, telAlternativo, correo);

                return cliente;

            }
            catch (Exception ex)
            {
                Console.WriteLine("Ocurrió un problema al ingresar un cliente: " + ex.Message);
                return null;
            }

        }

        public void EliminarCliente(int dniCliente) //Lo mismo que arriba, se usa para eliminar un cliente de la lista
        {
            try
            {

                Cliente clienteExistente = BuscarCliente(dniCliente);

                if (clienteExistente == null)
                {
                    Console.WriteLine("\nNingun cliente existe con ese dni");
                }
                else
                {
                    Console.WriteLine("\nCliente eliminado correctamente");
                    clientes.Remove(clienteExistente);
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al eliminar cliente: " + ex.Message);
            }
        }

        public Cliente BuscarCliente(int dniCliente)
        {
            Cliente clienteExistente = null; // Buscamos si el cliente existe en la lista:
            try
            {
                for (int i = 0; i < clientes.Count; i++)
                {
                    if (clientes[i].DNI == dniCliente)
                    {
                        clienteExistente = clientes[i]; //Asignamos el valor del cliente existente a la variable
                    }
                }

                if (clienteExistente == null)
                {
                    Console.WriteLine("\nNo existe ningun cliente con ese DNI");
                    return clienteExistente;
                }

                return clienteExistente;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Ocurrió un error al buscar cliente: " + ex.Message);
                return null;
            }
           

        }


        public Linea BuscarLinea(int numeroDeLinea) //Metodo corregido por Gemini
        {
            try
            {
                foreach (Cliente c in clientes) //Iteramos la lista de clientes
                {
                    foreach (Linea linea in c.Lineas) //Luego, iteramos la lista de lineas dentro del cliente
                    {
                        if (numeroDeLinea == linea.Numero)
                        {
                            return linea;
                        }
                    }
                }

                Console.WriteLine("\nNo existe ninguna linea con ese Número");
                return null;
            }catch(Exception ex)
            {
                Console.WriteLine("Error al buscar linea");
                return null;
            }
        }

        public void TransferirSaldo(int numOrigen, int numDestino, double monto)
        {         

            try
            {
                Linea lineaOrigen = BuscarLinea(numOrigen);

                Linea lineaDestino = BuscarLinea(numDestino);

                if (lineaOrigen == null || lineaDestino == null)
                {
                    Console.WriteLine("\nUno de los numeros proporcionados no corresponden a ninguna linea");
                }
                else
                {
                    if (lineaOrigen.DNI == lineaDestino.DNI) //VALIDAMOS QUE CORRESPONDAN AL MISMO DNI (CLIENTE)
                    {
                        if (lineaOrigen.SaldoDisponible < monto)
                        {
                            throw new SaldoInsuficienteException();
                        }
                        else
                        {
                            lineaOrigen.SaldoDisponible -= monto;
                            lineaDestino.SaldoDisponible += monto;
                            Console.WriteLine("\nTransferencia exitosa");
                        }
                    }
                    else
                    {
                        Console.WriteLine("\nLos numeros enviados corresponden a 2 cliente distintos");
                    }
                    
                }
            }catch(SaldoInsuficienteException six)
            {
                Console.WriteLine("Saldo insuficiente para realizar la transferencia");
            
            }catch(Exception ex)
            {
                Console.WriteLine("Error al transferir saldo " + ex.Message);
            }

        }
    }
}

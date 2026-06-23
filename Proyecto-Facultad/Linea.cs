using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_Facultad
{
    public class Linea
    {
        private int numero;
        private string planContratado;
        private double saldoDisponible;
        private bool estadoDeLinea;
        private int dni;

        public Linea(int numero, string planContratado, int dni)
        {
            this.numero = numero;
            this.planContratado = planContratado;
            this.saldoDisponible = 100;
            this.estadoDeLinea = true;
            this.dni = dni;
        }

        public int Numero
        {
            get { return numero; }
            set { numero = value; }
        }

        public string PlanContratado
        {
            get { return planContratado; }
            set { planContratado = value; }
        }

        public double SaldoDisponible
        {
            get { return saldoDisponible; }
            set { saldoDisponible = value; }
        }

        public bool EstadoDeLinea
        {
            get { return estadoDeLinea; }
            set { estadoDeLinea = value; }
        }

        public int DNI
        {
            get { return dni; }
            set { dni = value; }
        }

        public void RealizarLlamado()
        {
            try
            {
                //Validamos si la línea está activa 
                if (estadoDeLinea == false)
                {
                    Console.WriteLine("\nLlamada fallida: La línea está suspendida.");
                }

                else if (saldoDisponible >= 10) //Validamos que el saldo sea suficiente
                {
                    Console.WriteLine("\nLlamada realizada (costo $10).");
                    saldoDisponible -= 10;
                    Console.WriteLine("\nSaldo restante: ${0}", saldoDisponible);
                }
                else
                {
                    throw new SaldoInsuficienteException();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al realizar llamada: " + ex.Message);
            }
            
        }


        public void EnviarMensaje()
        {
            try
            {
                if (estadoDeLinea == false)
                {
                    Console.WriteLine("\nMensaje fallido: La línea está suspendida.");
                }
                else if (this.saldoDisponible >= 2)
                {
                    Console.WriteLine("\nMensaje enviado (costo $2).");
                    saldoDisponible -= 2;
                    Console.WriteLine("\nSaldo restante: ${0}", saldoDisponible);
                }
                else
                {
                    throw new SaldoInsuficienteException();
                }
            }catch(Exception ex)
            {
                Console.WriteLine("Error al enviar mensaje: " + ex.Message);
            }
            
        }

        
        public void RecargarSaldo(double monto)
        {
            try
            {
                saldoDisponible += monto;
                Console.WriteLine("\nRecarga exitosa.");
                Console.WriteLine("\nNuevo saldo: ${0}", saldoDisponible);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error al recargar saldo: " + ex.Message);
            }

            
        }
        public void SuspenderReactivarLinea()
        {

            try
            {
                
                if (estadoDeLinea == true)
                {
                    estadoDeLinea = false;
                    Console.WriteLine("\nLa línea {0} ha sido SUSPENDIDA.", numero);
                    
                }
                else
                {
                    estadoDeLinea = true;
                    Console.WriteLine("\nLa línea {0} ha sido REACTIVADA.", numero);
                }
            }
            catch (Exception ex)
            {

                Console.WriteLine("Error al suspender o reactivar una linea: " + ex.Message);
            }            
        }
    }
}
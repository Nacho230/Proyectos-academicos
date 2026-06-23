using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Proyecto_Facultad
{
     public class Cliente
     {
        private string nombre;
        private int dni;
        private string direccion;
        private int telefonoAlternativo;
        private string correoElectronico;
        private List<Linea> lineas;

        public Cliente(string nombre, int dni, string direccion, int telefonoAlternativo, string correoElectronico)
        {
            this.nombre=nombre;
            this.dni=dni;
            this.direccion=direccion;
            this.telefonoAlternativo=telefonoAlternativo;
            this.correoElectronico=correoElectronico;
            this.lineas = new List<Linea>();
        }

        public string Nombre
        {
            get{return nombre;}
            set{nombre=value;}
        }

        public int DNI
        {
            get{return dni;}
            set{dni=value;}
        }

        public string Direccion
        {
            get{return direccion;}
            set{direccion=value;}
        }

        public int TelefonoAlternativo
        {
            get{return telefonoAlternativo;}
            set{telefonoAlternativo=value;}
        }

        public string CorreoElectronico
        {
            get{return correoElectronico;}
            set{correoElectronico=value;}
        }

        public List<Linea> Lineas
        {
            set{lineas = value;}

            get{return lineas;}
        }

        public void MostrarDatos()
        {
            Console.WriteLine("Nombre:{0}, \nDNI:{1}, \nDirección:{2}, \nTelefono:{3}, \nCorreo Electronico:{4}", nombre, dni, direccion, telefonoAlternativo, correoElectronico);
        }
    }
}

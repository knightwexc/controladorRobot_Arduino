#include <Servo.h>

int Grabar = 2;
int Reproducir = 4;
int Resetear = 7;  

int servoPinCodo = 11;
int servoPinPinza = 10;
int servoPinBase = 9;


int POTBase = A0;
int POTCodo = A1;
int POTPinza = A2;

int MovGuardado[20][3];

int i = 0;
int j = 0;
int iGrabar = 0;
int jGrabar = 0;
int iGrabarActual = 0;
int iReproducir = 0;
int jReproducir = 0;

int valorPOTBase;
int anguloBase;
int valorPOTCodo;
int anguloCodo;
int valorPOTPinza;
int anguloPinza;

int ultimaFila = 0; 
int anguloBaseRep = 0;
int anguloCodoRep = 0;
int anguloPinzaRep = 0;
int angulo1 = 0;
int angulo2 = 0;
int angulo3 = 0;

Servo Base;
Servo Codo;
Servo Pinza;

void setup()
{
  Serial.begin(9600);
  pinMode(Grabar, INPUT_PULLUP);
  pinMode(Reproducir, INPUT_PULLUP);
  pinMode(Resetear, INPUT_PULLUP);

  pinMode(POTBase, INPUT); 
  pinMode(POTCodo, INPUT);
  pinMode(POTPinza, INPUT);

  Base.attach(servoPinBase); 
  Codo.attach(servoPinCodo);
  Pinza.attach(servoPinPinza);

  for (i = 0; i < 20; i++)
  {
    for (j = 0; j < 3; j++)
    {
      MovGuardado[i][j] = 0;
    }
  }
  Serial.println("Inicializado: ");
}

void loop()
{

  if (digitalRead(Reproducir) == HIGH) 
  {
    valorPOTBase = analogRead(POTBase);
    anguloBase = map(valorPOTBase, 0, 1023, 0, 180);
    Base.write(anguloBase);
    valorPOTCodo = analogRead(POTCodo);
    anguloCodo = map(valorPOTCodo, 0, 1023, 0, 180);
    Codo.write(anguloCodo);
    valorPOTPinza = analogRead(POTPinza);
    anguloPinza = map(valorPOTPinza,0, 1023, 0, 180);
    Pinza.write(anguloPinza);
  }

  if (digitalRead(Resetear) == LOW)
  {
    Serial.println("Borrando, espere...");
    delay(100);
    for (i = 0; i < 20; i++)
    {
      for (j = 0; j < 3; j++)
      {
        MovGuardado[i][j] = 0;
      }
    }
    Serial.println("Borrado Listo");
    iGrabar = 0;
    ultimaFila = 0;
  }

  if ((digitalRead(Grabar) == LOW) && (ultimaFila != 19))
  {
   
    for (iGrabar; iGrabar <= ultimaFila; iGrabar++)
    {
       Serial.print("Grabando posicion: ");
       Serial.println(iGrabar);
        delay(100);
      for (jGrabar = 0; jGrabar < 3; jGrabar++)
      {
        if (jGrabar == 0) 
        {
          MovGuardado[iGrabar][jGrabar] = anguloBase;
          delay(300);
        }
      
        if (jGrabar == 1)
        {
          MovGuardado[iGrabar][jGrabar] = anguloCodo;
          delay(300);
        }
        if (jGrabar == 2)
        {
          MovGuardado[iGrabar][jGrabar] = anguloPinza;
          delay(300);
        }
       
      }
       Serial.println("Posiciones guardadas");
    }
    ultimaFila += 1;

    if (ultimaFila == 19)
    {
      Serial.println("Maximo de posiciones guardadas, no se pueden añadir mas posiciones");
    }
  }

  if ((digitalRead(Grabar) == LOW) && (ultimaFila == 19))
  {
    Serial.println("Maximo de posiciones guardadas, no se pueden añadir mas posiciones");
  }

  if (digitalRead(Reproducir) == LOW) 
  {
    delay(100);
    angulo1 = anguloBase; 
    angulo2 = anguloCodo;
    angulo3 = anguloPinza;

    for (iReproducir = 0; iReproducir < iGrabar; iReproducir++) 
    {
      for (jReproducir = 0; jReproducir < 3; jReproducir++) 
        delay(100);
        if (jReproducir == 0)
        {
          Serial.println((String)"Reproduciendo BASE posicion. -J: "+jReproducir+" -I:"+ iReproducir);
          delay(100);
          if (angulo1 < MovGuardado[iReproducir][jReproducir] && jReproducir==0) 
          {
            for (anguloBaseRep = angulo1; anguloBaseRep <= MovGuardado[iReproducir][jReproducir]; anguloBaseRep++) 
            {
              Base.write(anguloBaseRep);
              delay(15);
              angulo1 = anguloBaseRep;
            }
          }
          if (angulo1 > MovGuardado[iReproducir][jReproducir] && jReproducir==0) 
          {

            for (anguloBaseRep = angulo1; anguloBaseRep >= MovGuardado[iReproducir][jReproducir]; anguloBaseRep--)
            {
              Base.write(anguloBaseRep);
              delay(15);
              angulo1 = anguloBaseRep;
            }
          }
        }
        
        if (jReproducir == 1) 
          Serial.println((String)"Reproduciendo CODO posicion. -J: "+jReproducir+" -I:"+ iReproducir);
        {
          delay(100);

          if (angulo2 < MovGuardado[iReproducir][jReproducir] && jReproducir==1)
          {

            for (anguloCodoRep = angulo2; anguloCodoRep <= MovGuardado[iReproducir][jReproducir]; anguloCodoRep++)
            {
              Codo.write(anguloCodoRep);
              delay(15);
              angulo2 = anguloCodoRep;
            }
          }
          if (angulo2 > MovGuardado[iReproducir][jReproducir] && jReproducir==1)
          {

            for (anguloCodoRep = angulo2; anguloCodoRep >= MovGuardado[iReproducir][jReproducir]; anguloCodoRep--)
            {
              Codo.write(anguloCodoRep);
              delay(15);
              angulo2 = anguloCodoRep;
            }
          }
        }
        if (jReproducir == 2) 
        {
          Serial.println((String)"Reproduciendo PINZA posicion. -J: "+jReproducir+" -I:"+ iReproducir);
          delay(100);
          if (angulo3< MovGuardado[iReproducir][jReproducir] && jReproducir==2)
          {

            for (anguloPinzaRep = angulo3; anguloPinzaRep <= MovGuardado[iReproducir][jReproducir]; anguloPinzaRep++)
            {
              Pinza.write(anguloPinzaRep);
              delay(15);
              angulo3= anguloPinzaRep;
            }
          }
          if (angulo3> MovGuardado[iReproducir][jReproducir] && jReproducir==2)
          {

            for (anguloPinzaRep = angulo3; anguloPinzaRep >= MovGuardado[iReproducir][jReproducir]; anguloPinzaRep--)
            {
              Pinza.write(anguloPinzaRep);
              delay(15);
              angulo3= anguloPinzaRep;
            }
          }
        }
      }
    }
    delay(1000);              
    if (anguloBase > angulo1)
    {
      Serial.println("posicion inicial Base");
      for (angulo1; angulo1 <= anguloBase; angulo1++)
      {

        Base.write(angulo1);
        delay(15);
      }
    }

    if (anguloBase < angulo1)
    {
      for (angulo1; angulo1 >= anguloBase; angulo1--)
      {

        Base.write(angulo1);
        delay(15);
      }
    }

    if (anguloCodo > angulo2)
    {
      Serial.println("posicion inicial Codo");
      for (angulo2; angulo2 <= anguloCodo; angulo2++)
      {

        Codo.write(angulo2);
        delay(15);
      }
    }

    if (anguloCodo < angulo2)
    {
      for (angulo2; angulo2 >= anguloCodo; angulo2--)
      {

        Codo.write(angulo2);
        delay(15);
      }
    }
    if (anguloPinza > angulo3)
    {
      Serial.println("posicion inicial Pinza");
      for (angulo3; angulo3 <= anguloPinza; angulo3++)
      {

        Pinza.write(angulo3);
        delay(15);
      }
    }

    if (anguloPinza < angulo3)
    {
      for (angulo3; angulo3 >= anguloPinza; angulo3--)
      {

        Pinza.write(angulo3);
        delay(15);
      }
    }
  }

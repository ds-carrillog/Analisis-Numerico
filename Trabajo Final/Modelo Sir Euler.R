SIR.model <- function(t, b, g, n, c){
  require(deSolve) # Librería deSolve para resolver Sistemas de Ecuaciones Diferenciales
  init <- c(S=1-(c/n),I=c/n,R=0)
  parameters <- c(beta=b,gamma=g) #Parámetros
  time <- seq(0,t,by=1) #Se calculan los valores por cada día. Para hacerlo por día y medio cambiar el valor de 1 por 1/2
  eqn <- function(time,state,parameters){ #Ecuaciones del Sistema
    with(as.list(c(state,parameters)),{
      dS <- -beta*S*I #cambio en la proporción de los susceptibles(dS/dt)
      dI <- beta*S*I-gamma*I #cambio en la proporción de los infectados (dI/dt)
      dR <- gamma*I #cambio en la proporción de los recuperados (dR/dt)
      return(list(c(dS,dI,dR)))}) #lista con los resultados.
  }
  out<-ode(y=init,times=time,eqn,parms=parameters, method = "euler") #solución del sistema usando ode() de deSolve con el método euler. Para el método rk4 cambiar euler por rk4.
  out.df<-as.data.frame(out) #crea un dataframe del output de la función anterior.
  
  #print(out.df)
  
  require(ggplot2) #paquete ggplot para hacer gráficos lindos c:
  theme_set(theme_minimal())
  title <- bquote("Modelo SIR: Propagacion COVID-19 Santa Marta") #título del gráfico
  subtit<-bquote(list("Marzo 20/2020-Enero 01/2022", beta==.(parameters[1]),~gamma==.(parameters[2]), n==.(n), c==.(c))) #subtítulo con los parámetros usados.
  res<-ggplot(out.df,aes(x=time))+ #Plot con los resultados proporción vs días.
    ggtitle(bquote(atop(bold(.(title)),atop(bold(.(subtit))))))+ #poner título y subtítulo.
    geom_line(aes(y=S,colour="Susceptibles"))+ #línea del plot con los valores de S.
    geom_line(aes(y=I,colour="Infectados"))+ #línea del plot con los valores de I.
    geom_line(aes(y=R,colour="Recuperados"))+ #línea del plot con los valores de R.
    ylab(label="Proporción")+ #label del eje Y
    xlab(label="Tiempo (dias)")+ #label del eje X
    
    scale_colour_manual("Líneas",
                        breaks=c("Susceptibles","Infectados","Recuperados"),
                        values=c("seagreen","darkorchid","deeppink"))
  
  ###PUNTO 1.### Imprimir tabla con valores de proporción, se comenta al cambiar el número de días para evitar generar un archivo muy grande.
  
  # library(gridExtra)
  # pdf("Valores SIR 31 días.pdf", height=11, width=8.5)
  # grid.table(out.df(1:31))
  # dev.off()
  
  ###PUNTO 2.### Imprimir plot
  
  print(res)
  
  ###PUNTO 3.### Fecha estimada con la mayor cantidad de infectados.
  
  cat("\nLa proporción mayor de infectados estimada es: ", max(out.df$I), " (aproximadamente ", as.integer(max(out.df$I)*n)," personas) y se espera ocurra en el día: ", (which.max(out.df$I)-1), " ( aproximadamente 3 de marzo del 2021)." )
 
  ###PUNTO 4.### Calcular el porcentaje de población que llegaría a infectarse junto con el porcentaje de recuperación.
  
  cat("\n\nEl porcentaje estimado de población infectada para enero 01 del 2022 es: ", (out.df[653, 3]+out.df[653, 4])*100, "% y el porcentaje estimado de personas recuperadas es: ", (out.df[653, 4])*100, "%.")
  
  ###PUNTO 5.### Estimar la fecha en la que la epidemia estará controlada.
  
  indiceControl = g/(b*c)
  c <- which(out.df[['S']]<indiceControl)-1
  cat("\n\nApartir del día ", c[1] ," (aproximadamente marzo 27 del 2021) se estima que la epidemia estará controlada.")

}

SIR.model(652,0.06,0.021,479835,1.5)



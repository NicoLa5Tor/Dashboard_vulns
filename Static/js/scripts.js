// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var total = data.response.item.Total;

    // Calcular el porcentaje de AwaitAnalisis respecto al Total.
    var percentage = ((awaitAnalisis / total) * 100).toFixed(2);

    // Actualizar el div con el valor y el porcentaje obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(percentage + "% del total");
  });
});

// Esta función también se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis, Critical y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var critical = data.response.item.Critical;
    var total = data.response.item.Total;

    // Calcular los porcentajes de AwaitAnalisis y Critical respecto al Total.
    var awaitAnalisisPercentage = ((awaitAnalisis / total) * 100).toFixed(2);
    var criticalPercentage = ((critical / total) * 100).toFixed(2);

    // Actualizar los divs con los valores y los porcentajes obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(awaitAnalisisPercentage + "% del total");

    $("#criticalValue").text(critical);
    $("#criticalPercentage").text(criticalPercentage + "% del total");
  });
});

// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis, Critical, High y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var critical = data.response.item.Critical;
    var high = data.response.item.High;
    var total = data.response.item.Total;

    // Calcular los porcentajes de AwaitAnalisis, Critical y High respecto al Total.
    var awaitAnalisisPercentage = ((awaitAnalisis / total) * 100).toFixed(2);
    var criticalPercentage = ((critical / total) * 100).toFixed(2);
    var highPercentage = ((high / total) * 100).toFixed(2);

    // Actualizar los divs con los valores y los porcentajes obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(awaitAnalisisPercentage + "% del total");

    $("#criticalValue").text(critical);
    $("#criticalPercentage").text(criticalPercentage + "% del total");

    $("#highValue").text(high);
    $("#highPercentage").text(highPercentage + "% del total");
  });
});

// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis, Critical, High, Low y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var critical = data.response.item.Critical;
    var high = data.response.item.High;
    var low = data.response.item.Low;
    var total = data.response.item.Total;

    // Calcular los porcentajes de AwaitAnalisis, Critical, High y Low respecto al Total.
    var awaitAnalisisPercentage = ((awaitAnalisis / total) * 100).toFixed(2);
    var criticalPercentage = ((critical / total) * 100).toFixed(2);
    var highPercentage = ((high / total) * 100).toFixed(2);
    var lowPercentage = ((low / total) * 100).toFixed(2);

    // Actualizar los divs con los valores y los porcentajes obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(awaitAnalisisPercentage + "% del total");

    $("#criticalValue").text(critical);
    $("#criticalPercentage").text(criticalPercentage + "% del total");

    $("#highValue").text(high);
    $("#highPercentage").text(highPercentage + "% del total");

    $("#lowValue").text(low);
    $("#lowPercentage").text(lowPercentage + "% del total");
  });
});

// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis, Critical, High, Low, Medium y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var critical = data.response.item.Critical;
    var high = data.response.item.High;
    var low = data.response.item.Low;
    var medium = data.response.item.Medium;
    var total = data.response.item.Total;

    // Calcular los porcentajes de AwaitAnalisis, Critical, High, Low y Medium respecto al Total.
    var awaitAnalisisPercentage = ((awaitAnalisis / total) * 100).toFixed(2);
    var criticalPercentage = ((critical / total) * 100).toFixed(2);
    var highPercentage = ((high / total) * 100).toFixed(2);
    var lowPercentage = ((low / total) * 100).toFixed(2);
    var mediumPercentage = ((medium / total) * 100).toFixed(2);

    // Actualizar los divs con los valores y los porcentajes obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(awaitAnalisisPercentage + "% del total");

    $("#criticalValue").text(critical);
    $("#criticalPercentage").text(criticalPercentage + "% del total");

    $("#highValue").text(high);
    $("#highPercentage").text(highPercentage + "% del total");

    $("#lowValue").text(low);
    $("#lowPercentage").text(lowPercentage + "% del total");

    $("#mediumValue").text(medium);
    $("#mediumPercentage").text(mediumPercentage + "% del total");
  });
});

// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de None y Total de la respuesta de la API.
    var none = data.response.item.None;
    var total = data.response.item.Total;

    // Calcular el porcentaje de None respecto al Total.
    var nonePercentage = ((none / total) * 100).toFixed(2);

    // Asegurarse de que siempre se muestren al menos 4 cifras significativas para el porcentaje de None si es muy pequeño.
    if (nonePercentage < 0.01) {
      nonePercentage = ((none / total) * 100).toPrecision(4);
    }

    // Actualizar los divs con los valores y el porcentaje obtenidos.
    $("#noneValue").text(none);
    $("#nonePercentage").text(nonePercentage + "% del total");
  });
});

// Esta función se ejecuta cuando el documento está completamente cargado y listo.
$(document).ready(function () {
  // Realizar una solicitud AJAX a tu API en Flask.
  $.getJSON("/api/data", function (data) {
    // Obtener los valores de AwaitAnalisis, Critical, High, Low, Medium, None y Total de la respuesta de la API.
    var awaitAnalisis = data.response.item.AwaitAnalisis;
    var critical = data.response.item.Critical;
    var high = data.response.item.High;
    var low = data.response.item.Low;
    var medium = data.response.item.Medium;
    var none = data.response.item.None;
    var total = data.response.item.Total;

    // Calcular los porcentajes de AwaitAnalisis, Critical, High, Low, Medium y None respecto al Total.
    var awaitAnalisisPercentage = ((awaitAnalisis / total) * 100).toFixed(2);
    var criticalPercentage = ((critical / total) * 100).toFixed(2);
    var highPercentage = ((high / total) * 100).toFixed(2);
    var lowPercentage = ((low / total) * 100).toFixed(2);
    var mediumPercentage = ((medium / total) * 100).toFixed(2);
    var nonePercentage = ((none / total) * 100).toFixed(2);

    // Actualizar los divs con los valores y los porcentajes obtenidos.
    $("#awaitAnalisisValue").text(awaitAnalisis);
    $("#awaitAnalisisPercentage").text(awaitAnalisisPercentage + "% del total");

    $("#criticalValue").text(critical);
    $("#criticalPercentage").text(criticalPercentage + "% del total");

    $("#highValue").text(high);
    $("#highPercentage").text(highPercentage + "% del total");

    $("#lowValue").text(low);
    $("#lowPercentage").text(lowPercentage + "% del total");

    $("#mediumValue").text(medium);
    $("#mediumPercentage").text(mediumPercentage + "% del total");

    $("#noneValue").text(none);
    $("#nonePercentage").text(nonePercentage + "% del total");

    // Actualizar el div del total.
    $("#totalValue").text(total);
  });
});

$(document).ready(function () {
  // Cambiar el ícono según el tipo de gráfica
  $("#chart-icon").removeClass().addClass("fas fa-chart-bar");

  // Realizar una solicitud AJAX a la ruta "/data" y crear una gráfica de barras con los datos recibidos.
  $.getJSON("/data", function (data) {
      // Obtener el contexto del elemento canvas con el ID "myChart".
      var ctx = document.getElementById("myChart").getContext("2d");
      // Crear una nueva gráfica de Chart.js.
      var myChart = new Chart(ctx, {
          type: "bar", // Tipo de gráfica
          data: data, // Datos de la gráfica
          options: {
              scales: {
                  y: {
                      beginAtZero: true, // La escala del eje y comienza en cero
                  },
              },
              plugins: {
                  legend: {
                      position: "top", // Posición de la leyenda
                      labels: {
                          padding: 20, // Espaciado entre etiquetas
                          font: {
                              size: 14, // Tamaño de fuente de las etiquetas
                          },
                      },
                  },
              },
              responsive: true, // La gráfica es responsiva
              maintainAspectRatio: false, // Mantener la proporción de aspecto
          },
      });
  });
});


// Realizar una solicitud fetch a la ruta "/data3" y crear otra gráfica de barras con los datos recibidos.
fetch("/data3")
  .then((response) => response.json()) // Convertir la respuesta a JSON
  .then((data) => {
    // Obtener el contexto del elemento canvas con el ID "poblacionChart".
    var ctx = document.getElementById("poblacionChart").getContext("2d");
    // Crear una nueva gráfica de Chart.js.
    var poblacionChart = new Chart(ctx, {
      type: "bar", // Tipo de gráfica
      data: data, // Datos de la gráfica
      options: {
        responsive: true, // La gráfica es responsiva
        maintainAspectRatio: false, // Mantener la proporción de aspecto
        scales: {
          y: {
            beginAtZero: true, // La escala del eje y comienza en cero
          },
        },
      },
    });
  });

document.addEventListener("DOMContentLoaded", function () {
  // Añadir un manejador de eventos al formulario para manejar el evento de envío (submit).
  document
    .getElementById("cveForm")
    .addEventListener("submit", function (event) {
      // Prevenir el comportamiento por defecto del formulario (recarga de la página).
      event.preventDefault();

      // Obtener el valor del campo de entrada con el ID "cve_id".
      const cveId = document.getElementById("cve_id").value;

      // Mostrar el indicador de carga.
      showLoading(true);

      // Realizar una solicitud fetch a la API para obtener los datos del CVE.
      fetch(`/api/cve/${cveId}`)
        .then((response) => {
          // Si la respuesta no es exitosa, lanzar un error.
          if (!response.ok) {
            throw new Error("CVE no encontrado");
          }
          // Convertir la respuesta a formato JSON.
          return response.json();
        })
        .then(({ data, cvss_score }) => {
          // Obtener el div de resultados con el ID "result".
          const resultDiv = document.getElementById("result");

          // Actualizar el contenido del div con los datos obtenidos.
          resultDiv.innerHTML = `
                <h2 class="text-center">Resultado de consulta</h2>
                <div class="table-responsive">
                  <table class="table mt-4">
                    <thead>
                      <tr>
                        <th scope="col">CVE ID</th>
                        <th scope="col">Descripción</th>
                        <th scope="col">Publicado</th>
                        <th scope="col">Última modificación</th>
                        <th scope="col">CVSS Score</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>${data.id}</td>
                        <td>${data.summary}</td>
                        <td>${data.Published}</td>
                        <td>${data.Modified}</td>
                        <td>${cvss_score}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              `;

          // Ocultar el indicador de carga.
          showLoading(false);
        })
        .catch((error) => {
          // En caso de error, mostrar un mensaje de alerta.
          console.error("Error:", error);
          document.getElementById("result").innerHTML =
            '<div class="alert alert-danger" role="alert">' +
            error.message +
            "</div>";

          // Ocultar el indicador de carga.
          showLoading(false);
        });
    });

  // Función para limpiar los resultados.
  function clearResults() {
    // Limpiar el contenido del div de resultados.
    document.getElementById("result").innerHTML = "";

    // Limpiar el campo de entrada del CVE ID.
    document.getElementById("cve_id").value = "";

    // Ocultar el indicador de carga.
    showLoading(false);
  }

  // Función para mostrar u ocultar el indicador de carga.
  function showLoading(show) {
    // Mostrar el indicador de carga si "show" es true, de lo contrario, ocultarlo.
    document.getElementById("loading").style.display = show ? "block" : "none";

    // Mostrar los resultados si "show" es false, de lo contrario, ocultarlos.
    document.getElementById("result").style.display = show ? "none" : "block";
  }
});
$(document).ready(function () {
  // Cambiar el ícono según el tipo de gráfica
  $("#chart-icon").removeClass().addClass("fas fa-chart-line");

  // Realizar una solicitud AJAX a la ruta "/data2" para obtener los datos
  $.getJSON("/data2", function (data) {
    console.log("Datos recibidos:", data); // Mensaje de depuración
    if (data.error) {
      console.error(data.error);
      return;
    }

    // Nombres de los meses en español
    var monthNames = [
      "Enero",
      "Febrero",
      "Marzo",
      "Abril",
      "Mayo",
      "Junio",
      "Julio",
      "Agosto",
      "Septiembre",
      "Octubre",
      "Noviembre",
      "Diciembre",
    ];

    var labels = [];
    var values = [];

    // Procesar los datos para obtener las etiquetas y valores del gráfico
    data.forEach(function (item) {
      var parts = item.mes.split("-");
      var year = parts[0];
      var month = parts[1];
      labels.push(monthNames[parseInt(month) - 1] + " " + year);
      values.push(item.valor);
    });

    console.log("Etiquetas:", labels); // Mensaje de depuración
    console.log("Valores:", values); // Mensaje de depuración

    // Obtener el contexto del canvas con el ID "line-chart"
    var ctx = document.getElementById("line-chart").getContext("2d");
    // Crear una nueva gráfica de línea con Chart.js
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Cantidad de Vulnerabilidades",
            data: values,
            fill: true,
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 2,
            tension: 0.4,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Cantidad de Vulnerabilidades",
            },
          },
          x: {
            title: {
              display: true,
              text: "Mes",
            },
          },
        },
        interaction: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "nearest",
          intersect: true,
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: function (context) {
                var label = context.dataset.label || "";
                if (label) {
                  label += ": ";
                }
                label += context.parsed.y;

                if (context.parsed.y !== null) {
                  var index = context.dataIndex;
                  var currentMonth = data[index];
                  var previousMonth = data[index - 1] || {
                    valor: currentMonth.valor,
                  };
                  var percentageChange =
                    ((currentMonth.valor - previousMonth.valor) /
                      (previousMonth.valor || 1)) *
                    100;
                  var comparison =
                    currentMonth.valor > previousMonth.valor
                      ? "aumento"
                      : "disminución";
                  label +=
                    " (" +
                    comparison +
                    " del " +
                    Math.abs(percentageChange).toFixed(2) +
                    "% respecto a " +
                    (previousMonth.mes || "inicio") +
                    ")";
                }
                return label;
              },
            },
          },
        },
      },
    });

    // Ajustar el tamaño del canvas al contenedor
    function resizeCanvas() {
      var canvas = document.getElementById("line-chart");
      canvas.style.width = "100%";
      canvas.style.height = "100%";
    }

    // Llamar a resizeCanvas() cuando cambie el tamaño de la ventana
    window.addEventListener("resize", resizeCanvas, false);

    // Llamar a resizeCanvas() una vez al principio para establecer el tamaño inicial
    resizeCanvas();
  }).fail(function (jqXHR, textStatus, errorThrown) {
    console.error("Error al obtener los datos:", textStatus, errorThrown);
  });
});
document.addEventListener("DOMContentLoaded", function () {
  // Realizar una solicitud a la ruta "/data5" para obtener el total de vulnerabilidades.
  fetch("/data5")
      .then((response) => response.json()) // Convertir la respuesta a JSON.
      .then((data) => {
          // Actualizar el contenido del elemento con ID "vulnerabilityCount" con el total de vulnerabilidades.
          document.getElementById("vulnerabilityCount").textContent = data.total_vulnerabilities;
      })
      .catch((error) => console.error("Error al cargar los datos de vulnerabilidades:", error)); // Manejar errores.

  // Realizar una solicitud a la ruta "/data6" para obtener la máquina más vulnerable.
  fetch("/data6")
      .then((response) => response.json()) // Convertir la respuesta a JSON.
      .then((data) => {
          // Actualizar el contenido del elemento con ID "mostVulnerableMachine" con el nombre de la máquina.
          document.getElementById("mostVulnerableMachine").textContent = data.machine_name;
      })
      .catch((error) => console.error("Error al cargar los datos de la máquina más vulnerable:", error)); // Manejar errores.

  // Realizar una solicitud a la ruta "/data7" para obtener la máquina menos vulnerable.
  fetch("/data7")
      .then((response) => response.json()) // Convertir la respuesta a JSON.
      .then((data) => {
          // Actualizar el contenido del elemento con ID "leastVulnerableMachine" con el nombre de la máquina.
          document.getElementById("leastVulnerableMachine").textContent = data.machine_name;
      })
      .catch((error) => console.error("Error al cargar los datos de la máquina menos vulnerable:", error)); // Manejar errores.
});
document.addEventListener("DOMContentLoaded", function () {
  fetch("/top-vulnerabilities")
    .then((response) => response.json())
    .then((data) => {
      const ctx = document
        .getElementById("vulnerabilitiesChart")
        .getContext("2d");

      const names = data.map((v) => v.name);
      const severities = data.map((v) => v.severity);

      const colors = [
        "rgba(255, 159, 64, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(255, 206, 86, 0.2)",
        "rgba(75, 192, 192, 0.2)",
        "rgba(153, 102, 255, 0.2)",
        "rgba(255, 99, 132, 0.2)",
        "rgba(199, 199, 199, 0.2)",
        "rgba(83, 102, 255, 0.2)",
        "rgba(40, 159, 64, 0.2)",
        "rgba(143, 162, 235, 0.2)",
      ];
      const borderColors = colors.map((color) => color.replace("0.2", "1"));

      const chart = new Chart(ctx, {
        type: "doughnut",
        data: {
          labels: names,
          datasets: [
            {
              label: "Severidad",
              data: severities,
              backgroundColor: colors,
              borderColor: borderColors,
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: false,
          plugins: {
            tooltip: {
              callbacks: {
                label: function (tooltipItem) {
                  return `Severidad: ${tooltipItem.raw}`;
                },
                afterLabel: function (tooltipItem) {
                  return `Vulnerabilidad: ${tooltipItem.label}`;
                },
              },
            },
          },
        },
      });

      const tableBody = document.getElementById("vulnerabilitiesTable");

      data.forEach((v) => {
        const row = `<tr><td>${v.name}</td><td>${v.severity}</td><td>${v.description}</td></tr>`;
        tableBody.innerHTML += row;
      });
    })
    .catch((error) => console.error("Error al cargar los datos:", error));
});

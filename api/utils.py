def interpret_cluster(cluster):

    mapping = {
        0: {
            "segmento": "Clientes moderados",
            "perfil": {
                "edad": "40-60",
                "ingresos": "Medios",
                "gasto": "Medio"
            },
            "estrategias": [
                "Mantener engagement",
                "Ofrecer descuentos personalizados"
            ]
        },
        1: {
            "segmento": "Clientes de alto valor",
            "perfil": {
                "edad": "30-50",
                "ingresos": "Altos",
                "gasto": "Alto"
            },
            "estrategias": [
                "Ofertas premium",
                "Programas VIP",
                "Eventos exclusivos"
            ]
        },
        2: {
            "segmento": "Jóvenes con alto gasto",
            "perfil": {
                "edad": "20-30",
                "ingresos": "Bajos-Medios",
                "gasto": "Alto"
            },
            "estrategias": [
                "Campañas en redes sociales",
                "Productos de tendencia",
                "Marketing con influencers"
            ]
        },
        3: {
            "segmento": "Clientes promedio",
            "perfil": {
                "edad": "25-45",
                "ingresos": "Medios",
                "gasto": "Medio"
            },
            "estrategias": [
                "Promociones generales",
                "Fidelización básica"
            ]
        },
        4: {
            "segmento": "Altos ingresos, bajo gasto",
            "perfil": {
                "edad": "35-55",
                "ingresos": "Altos",
                "gasto": "Bajo"
            },
            "estrategias": [
                "Incentivar gasto",
                "Ofertas personalizadas",
                "Upselling"
            ]
        },
        5: {
            "segmento": "Clientes de bajo valor",
            "perfil": {
                "edad": "30-60",
                "ingresos": "Bajos",
                "gasto": "Bajo"
            },
            "estrategias": [
                "Optimizar costes",
                "Campañas masivas low-cost"
            ]
        }
    }

    return mapping.get(cluster, {"segmento": "Desconocido"})
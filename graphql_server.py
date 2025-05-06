# ejemplo de graphQL con Ariadne
from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        saludo(nombre: String!): String!
    }
""")

query = QueryType()

@query.field("saludo")
def resolve_saludo(_, info, nombre):
    return f"Hola, {nombre} desde GraphQL!"

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)
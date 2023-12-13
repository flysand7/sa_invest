
POSTGRES_URL='postgres://invest_crm:fdc804cd@localhost:5433/invest_crm?sslmode=disable'

create:
	./migrate create -ext sql -dir db/migrations -seq create_a

up:
	./migrate -database ${POSTGRES_URL} -path ./db/migrations up

down:
	./migrate -database ${POSTGRES_URL} -path ./db/migrations down

drop:
	./migrate -database ${POSTGRES_URL} -path ./db/migrations drop -f

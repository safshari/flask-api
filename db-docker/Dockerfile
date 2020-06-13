FROM alpine:3.10
RUN apk add --update sqlite
RUN mkdir /db
WORKDIR /db

ENTRYPOINT ["sqlite3"]
CMD ["test.db","create table test(id string, height float, width float, framecount int, fps int, timestamp string);"]
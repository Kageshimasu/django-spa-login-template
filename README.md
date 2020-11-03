## 概要
カスタムユーザモデルで作成された環境でJWTによる認証ができるテンプレート。

## 環境構築

```
docker-compose up -d
```

## 動作確認
アカウント作成
```
curl -i -X POST -d "{\"username\":\"admin\", \"email\":\"admin@example.com\",\"password\":\"admin\"}" http://127.0.0.1:8000/auth_api/createAccount
```

JWT発行
```
 curl http://localhost:8000/auth_api/token -d "username=admin&email=admin@example.com&password=admin"
```

認証テスト
```
 curl -X POST http://localhost:8000/auth_api/hello -H "Authorization: JWT {access token}"
```

# Backend — E-commerce API

REST API built with Express 5, TypeScript, and Prisma.

## Tech Stack

- **Runtime**: Node.js
- **Framework**: Express 5
- **Language**: TypeScript
- **ORM**: Prisma (SQLite)
- **Validation**: Zod
- **Auth**: JWT + bcrypt
- **Testing**: Jest + Supertest
- **Dev server**: ts-node-dev

## Project Structure

```
src/
├── app.ts                  # Express app setup
├── server.ts               # Entry point
├── config/
│   ├── db.ts               # Database connection
│   └── env.ts              # Environment variables
├── middlewares/
│   ├── auth.middleware.ts   # JWT authentication
│   └── error.middleware.ts  # Error handling
├── modules/                # Feature-based modules
│   ├── addresses/
│   ├── analytics/
│   ├── auth/
│   ├── cart/
│   ├── categories/
│   ├── notifications/
│   ├── orders/
│   ├── payment_proofs/
│   ├── payments/
│   ├── products/
│   ├── reviews/
│   ├── shipments/
│   ├── stores/
│   ├── uploads/
│   └── users/
├── types/                  # TypeScript type declarations
└── utils/
    ├── hash.ts             # Password hashing
    └── jwt.ts              # JWT utilities
```

Each module follows a consistent pattern:
- `*.controller.ts` — Request handlers
- `*.service.ts` — Business logic
- `*.model.ts` — Prisma client queries
- `*.dto.ts` — Zod validation schemas
- `*.routes.ts` — Route definitions

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start dev server with hot reload |
| `npm run build` | Compile TypeScript |
| `npm start` | Start production server |
| `npm test` | Run tests with Jest |
| `npm run prisma:generate` | Generate Prisma client |
| `npm run prisma:migrate` | Run database migrations |
| `npm run prisma:studio` | Open Prisma Studio |

## Environment Variables

```env
DATABASE_URL="file:./dev.db"
JWT_SECRET="your-secret-key"
```

## Data Model

The schema includes: Users, Stores, Products, Categories, Cart, Orders, Payments, PaymentProofs, Shipments, Reviews, Addresses, Notifications, AnalyticsEvents, and Uploads.

## API Endpoints

- `POST /api/auth/register` — Register a new user
- `POST /api/auth/login` — Login
- `GET /api/products` — List products
- `GET /api/products/:id` — Get product details
- `GET /api/categories` — List categories
- `POST /api/orders` — Create an order
- `GET /api/orders/:id` — Get order details
- *(More endpoints available per module)*

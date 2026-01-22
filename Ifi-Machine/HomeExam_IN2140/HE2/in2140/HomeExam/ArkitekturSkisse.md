```mermaid

graph TD
    A[Start] --> B[L2 - Data Link Layer]
    B --> C[L4 - Transport Layer]
    C --> D[L5 - Application Layer]
    
    %% L2 Details
    subgraph L2 [L2 - Data Link Layer]
        B1[UDP Socket] --> B2[L2 Frame Header]
        B2 --> B3[Checksum Calculation]
        B3 --> B4[Data Transfer to L4]
        B1 --> B5[Frame Reception]
        B5 --> B6[Checksum Validation]
        B6 --> B7[Transfer Data to L4]
    end

    %% L4 Details
    subgraph L4 [L4 - Transport Layer]
        C1[Packet Send Stop-and-Wait] --> C2[Packet Header with SeqNum and AckNo]
        C2 --> C3[Data Sending to L2]
        C3 --> C4[Waiting for Ack]
        C4 --> C5[Resend Packet if No Ack]
        C1 --> C6[Packet Reception]
        C6 --> C7[Packet Header Parsing]
        C7 --> C8[Send Ack to L2]
    end

    %% L5 Details
    subgraph L5 [L5 - Application Layer]
        D1[Send MAZE Request] --> D2[Receive Maze from Server]
        D2 --> D3[Solve Maze]
        D3 --> D4[Send Solved Maze to Server]
        D4 --> D5[Send QUIT Message]
        D5 --> D6[End Connection]
    end

    %% Connections between Layers
    B4 --> C1
    B7 --> C6
    C5 --> D1

    style L2 fill:#f9f,stroke:#333,stroke-width:2px
    style L4 fill:#bbf,stroke:#333,stroke-width:2px
    style L5 fill:#fbf,stroke:#333,stroke-width:2px

    classDef L2 fill:#f9f,stroke:#333,stroke-width:2px;
    classDef L4 fill:#bbf,stroke:#333,stroke-width:2px;
    classDef L5 fill:#fbf,stroke:#333,stroke-width:2px;
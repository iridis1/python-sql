SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- Simulates source database

CREATE TABLE [dbo].[Color](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](32) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Color] ADD  CONSTRAINT [PK_Color] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Shirt](
	[Id] [int] NOT NULL,
	[Size] [int] NULL,
	[Color_Id] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Shirt] ADD  CONSTRAINT [PK_Shirt] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Shirt]  WITH CHECK ADD  CONSTRAINT [FK_Shirt_Color] FOREIGN KEY([Color_Id])
REFERENCES [dbo].[Color] ([Id])
GO
ALTER TABLE [dbo].[Shirt] CHECK CONSTRAINT [FK_Shirt_Color]
GO

-- Datavault (limited implementation, hub and satellite tables only)

CREATE TABLE [dbo].[H_Color](
	[Id] [int] NOT NULL,
	[Code] [nvarchar](2) NOT NULL,
	[Timestamp] [datetime] NOT NULL,
	[Source] [nvarchar](32) NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[H_Color] ADD  CONSTRAINT [PK_H_Color] PRIMARY KEY NONCLUSTERED 
(
	[Id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO

GO
CREATE TABLE [dbo].[S_Color](
	[Color_Id] [int] NOT NULL,
	[Name] [nvarchar](32) NOT NULL,
	[Timestamp] [datetime] NOT NULL,
	[Source] [nvarchar](32) NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[S_Color] ADD  CONSTRAINT [PK_S_Color] PRIMARY KEY CLUSTERED 
(
	[Color_Id] ASC,
	[Timestamp] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO




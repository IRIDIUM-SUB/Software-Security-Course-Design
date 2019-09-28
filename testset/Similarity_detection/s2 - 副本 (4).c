#include<stdio.h>
#include<string.h>
//end->evd
typedef struct{	// 随从 
	int hea;
	int att;
}Role;

typedef struct{	//英雄 
	int hea;
	Role ro[7]; 
	int num;
}Player;

int nowplayer;	//当前操控者 0 或 1 
Player player[2];	// 双方 

void summon(int point, Role addrole)	// 召唤随从 
{
	Role temp = addrole;
	for(int i = point; i < 7-1; i ++)
	{
		Role tempin = temp;
		temp = player[nowplayer].ro[point];
		player[nowplayer].ro[point] = tempin;
		
		point ++;
	}
	player[nowplayer].ro[point] = temp;
	player[nowplayer].num ++;
}

void move(int point, int play)	//攻击死亡后左移动 
{
	for(int i = point; i < player[play].num-1; i ++)
	{
		player[play].ro[point] = player[play].ro[point+1];
	}
	player[play].num --;
}

void attack(int point1, int point2)	//攻击 
{
	int enemy;
	if(nowplayer == 0)
	{
		enemy = 1;
	} else {
		enemy = 0;
	}
	
	if(point2 == -1)	// 进攻敌方英雄 
	{
		player[enemy].hea = player[enemy].hea - player[nowplayer].ro[point1].att;
		return ;
	}
	
	player[nowplayer].ro[point1].hea = player[nowplayer].ro[point1].hea - player[enemy].ro[point2].att;
	player[enemy].ro[point2].hea = player[enemy].ro[point2].hea - player[nowplayer].ro[point1].att;
	
	if(player[nowplayer].ro[point1].hea <= 0)
	{
		move(point1, nowplayer);
	}
	if(player[enemy].ro[point2].hea <= 0)
	{
		move(point2, enemy);
	}
	
}

void evd()	// 切换操控者 
{
	if(nowplayer == 0)
	{
		nowplayer = 1;
	} else {
		nowplayer = 0;
	}
}

int main()
{
	int n;
	int win = 0;
	
	nowplayer = 0;
	player[0].hea = 30;
	player[1].hea = 30;
	player[0].num = 0;
	player[1].num = 0;
	scanf("%d", &n);
	
	for(int i = 0; i < n; i ++)
	{
		char use[10];
		scanf("%s", use);

		if(strcmp(use, "summon") == 0)
		{
			Role addrole;
			int point;
			scanf("%d %d %d", &point, &addrole.att, &addrole.hea);
			summon(point-1, addrole);
		}
		else if(strcmp(use, "attack") == 0)
		{
			int f, t;
			scanf("%d %d", &f, &t);
			attack(f-1, t-1);
			if(player[0].hea <= 0){
				win = 1;
				break;
			}
			else if(player[1].hea <= 0){
				win = -1;
				break;
			}
			
		}
		else if(strcmp(use, "evd") == 0)
		{
			evd();
		}

	}
	
	printf("%d\n", win);
	printf("%d\n", player[0].hea);
	printf("%d\n", player[0].num);
	for(int i = 0; i < player[0].num; i ++)
		printf("%d ", player[0].ro[i].hea);
	printf("\n%d\n", player[1].hea);
	printf("\n%d\n", player[1].num);
	for(int i = 0; i < player[1].num; i ++)
		printf("%d ", player[1].ro[i].hea);

	return 0;
}
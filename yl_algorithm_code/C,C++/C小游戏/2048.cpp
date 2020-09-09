#include <time.h>   /* �����趨�������������Ҫ��time()���� */
#include <stdio.h>  /* ����C��IO��д���� */
#include <stdlib.h> /* ����C��׼��Ĺ��� */

#ifdef _WIN32

/* ����Windowsƽ̨��غ�������������̨��������������趨�ȹ��� */
#include <conio.h>
#include <windows.h>
#include <io.h>
#include <direct.h>
#include <Shlobj.h>

#else

/* ����Linuxƽ̨��غ�������������̨��������������趨�ȹ��� */
#include <termio.h>
#include <unistd.h>
#include <bits/signum.h>
#include <signal.h>

#define KEY_CODE_UP    0x41
#define KEY_CODE_DOWN  0x42
#define KEY_CODE_LEFT  0x44
#define KEY_CODE_RIGHT 0x43
#define KEY_CODE_QUIT  0x71

struct termios old_config; /* linux���ն��������ñ��� */

#endif

static char config_path[4096] = {0}; /* �����ļ�·�� */

static void init_game();    /* ��ʼ����Ϸ */
static void loop_game();    /* ��Ϸѭ�� */
static void reset_game();   /* ������Ϸ */
static void release_game(int signal); /* �ͷ���Ϸ */

static int read_keyboard();

static void move_left();  /* ���� */
static void move_right(); /* ���� */
static void move_up();    /* ���� */
static void move_down();  /* ���� */

static void add_rand_num();    /* ������������������н�����2��4������֮����Ϊ9:1 */
static void check_game_over(); /* ����Ƿ������Ϸ���趨��Ϸ������־ */
static int get_null_count();   /* ��ȡ��Ϸ����Ͽ�λ������ */
static void clear_screen();    /* ���� */
static void refresh_show();    /* ˢ�½�����ʾ */

static int board[4][4];     /* ��Ϸ������壬����Ϊ��ά���� */
static int score;           /* ��Ϸ�÷� */
static int best;            /* ��Ϸ��߷� */
static int if_need_add_num; /* �Ƿ���Ҫ�����������־��1��ʾ��Ҫ��0��ʾ����Ҫ */
static int if_game_over;    /* �Ƿ���Ϸ������־��1��ʾ��Ϸ������0��ʾ���� */
static int if_prepare_exit; /* �Ƿ�׼���˳���Ϸ��1��ʾ�ǣ�0��ʾ�� */

/* main���� �������� */
int main(int argc, char *argv[]) {
	init_game();
	loop_game();
	release_game(0);
	return 0;
}

/* ��ȡ���� �������� */
int read_keyboard() {
#ifdef _WIN32
	return _getch();
#else
	int key_code;
	if (read(0, &key_code, 1) < 0) {
		return -1;
	}
	return key_code;
#endif
}

/* ��ʼ��Ϸ �������� */
void loop_game() {
	while (1) {
		int cmd = read_keyboard(); /* ���ձ�׼�������ַ����� */

		/* �ж��Ƿ�׼���˳���Ϸ */
		if (if_prepare_exit) {
			if (cmd == 'y' || cmd == 'Y') {
				/* �˳���Ϸ���������˳� */
				clear_screen();
				return;
			} else if (cmd == 'n' || cmd == 'N') {
				/* ȡ���˳� */
				if_prepare_exit = 0;
				refresh_show();
				continue;
			} else {
				continue;
			}
		}

		/* �ж��Ƿ��Ѿ������Ϸ */
		if (if_game_over) {
			if (cmd == 'y' || cmd == 'Y') {
				/* ������Ϸ */
				reset_game();
				continue;
			} else if (cmd == 'n' || cmd == 'N') {
				/* �˳���Ϸ���������˳�  */
				clear_screen();
				return;
			} else {
				continue;
			}
		}

		if_need_add_num = 0; /* ���趨��Ĭ����Ҫ�������������Ҫʱ���趨Ϊ1 */

#ifdef _WIN32
		/* ���������w��s��a��d�ַ����������������q�����˳� */
		switch (cmd) {
			case 'a':
			case 75:
				move_left();
				break;
			case 's':
			case 80:
				move_down();
				break;
			case 'w':
			case 72:
				move_up();
				break;
			case 'd':
			case 77:
				move_right();
				break;
			case 'q':
			case 27:
				if_prepare_exit = 1;
				break;
			default:
				continue;
		}
#else
		/* ����������������Ҽ�ͷ���������������q�����˳� */
		switch (cmd) {
			case 'a':
			case KEY_CODE_LEFT:
				move_left();
				break;
			case 's':
			case KEY_CODE_DOWN:
				move_down();
				break;
			case 'w':
			case KEY_CODE_UP:
				move_up();
				break;
			case 'd':
			case KEY_CODE_RIGHT:
				move_right();
				break;
			case KEY_CODE_QUIT:
				if_prepare_exit = 1;
				break;
			default:
				continue;
		}
#endif
		/* ���Ƶ÷ּ�¼ */
		if (score > best) {
			best = score;
			FILE *fp = fopen(config_path, "w");
			if (fp) {
				fwrite(&best, sizeof(best), 1, fp);
				fclose(fp);
			}
		}

		/* Ĭ��Ϊ��Ҫ���������ʱҲͬʱ��Ҫˢ����ʾ����֮��Ȼ */
		if (if_need_add_num) {
			add_rand_num();
			refresh_show();
		} else if (if_prepare_exit) {
			refresh_show();
		}
	}
}

/* ������Ϸ �������� */
void reset_game() {
	score = 0;
	if_need_add_num = 1;
	if_game_over = 0;
	if_prepare_exit = 0;

	/* �˽⵽��Ϸ��ʼ��ʱ���ֵ�������һ�����и�2���������������һ��2��������Ϊ0 */
	int n = rand() % 16;
	int i;
	for (i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; ++j) {
			board[i][j] = (n-- == 0 ? 2 : 0);
		}
	}

	/* ǰ���Ѿ�������һ��2������������һ�������2����4������֮��9:1 */
	add_rand_num();

	/* ������ˢ�½��沢��ʾ��ʱ�򣬽������Ѿ�Ĭ�ϳ������������֣������Ķ�Ϊ�գ�ֵΪ0�� */
	refresh_show();
}

/* ��������� �������� */
void add_rand_num() {
	srand((unsigned int) time(0));
	int n = rand() % get_null_count(); /* ȷ���ںδ���λ����������� */
	int i;
	for (i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; ++j) {
			/* ��λ�����ɵ�λ�� */
			if (board[i][j] == 0 && n-- == 0) {
				board[i][j] = (rand() % 10 ? 2 : 4); /* ��������2��4�����ɸ���Ϊ9:1 */
				return;
			}
		}
	}
}

/* ��ȡ��λ������ �������� */
int get_null_count() {
	int n = 0;
	int i;
	for (i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; ++j) {
			board[i][j] == 0 ? ++n : 1;
		}
	}
	return n;
}

/* �����Ϸ�Ƿ���� �������� */
void check_game_over() {
	int i;
	for (i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 3; ++j) {
			/* ���������Ƚϰ��ŵ�����Ԫ���Ƿ���ȣ������������Ϸ������ */
			if (board[i][j] == board[i][j + 1] || board[j][i] == board[j + 1][i]) {
				if_game_over = 0;
				return;
			}
		}
	}
	if_game_over = 1;
}

/*
 * �����ĸ�������ʵ�����������ƶ�ʱ�������ı仯�㷨
 * ������ƶ��ı���һ�����������������ı��������෴
 * �Ϻ����ƶ��ı���һ�����������������ı��������෴
 * ������ƶ��ı���Ҳһ������������Ǳ���ʱ�к��л���
*/

/*  ���� �������� */
void move_left() {
	/* ����i��������������±꣬�������ƶ�ʱ�������໥����������Ӱ�� */
	int i;
	for (i = 0; i < 4; ++i) {
		/* ����jΪ���±꣬����kΪ���Ƚϣ��ϲ�������±꣬ѭ������ʱk<j */
		int j, k;
		for (j = 1, k = 0; j < 4; ++j) {
			if (board[i][j] > 0) { /* �ҳ�k�����һ����Ϊ�յ���±�Ϊj��֮���������� */
				if (board[i][k] == board[i][j]) {
					/* ���1��k���j����ȣ���ʱ�ϲ����鲢�Ʒ� */
					score += board[i][k++] *= 2;
					board[i][j] = 0;
					if_need_add_num = 1; /* ��Ҫ�����������ˢ�½��� */
				} else if (board[i][k] == 0) {
					/* ���2��k��Ϊ�գ����j�ֵ��k��൱��j�����ƶ���k���� */
					board[i][k] = board[i][j];
					board[i][j] = 0;
					if_need_add_num = 1;
				} else {
					/* ���3��k�Ϊ�գ��Һ�j���ȣ���ʱ��j�ֵ��k+1��൱���ƶ���k+1��λ�� */
					board[i][++k] = board[i][j];
					if (j != k) {
						/* �ж�j���k���Ƿ�ԭ�ȾͰ���һ�����������j�ֵΪ�գ�ֵΪ0�� */
						board[i][j] = 0;
						if_need_add_num = 1;
					}
				}
			}
		}
	}
}

/* ���� �������� */
void move_right() {
	/* �������Ʋ��������������j��k��������� */
	int i;
	for (i = 0; i < 4; ++i) {
		int j, k;
		for (j = 2, k = 3; j >= 0; --j) {
			if (board[i][j] > 0) {
				if (board[i][k] == board[i][j]) {
					score += board[i][k--] *= 2;
					board[i][j] = 0;
					if_need_add_num = 1;
				} else if (board[i][k] == 0) {
					board[i][k] = board[i][j];
					board[i][j] = 0;
					if_need_add_num = 1;
				} else {
					board[i][--k] = board[i][j];
					if (j != k) {
						board[i][j] = 0;
						if_need_add_num = 1;
					}
				}
			}
		}
	}
}

/* ���� �������� */
void move_up() {
	/* �������Ʋ�����������������л�������� */
	int i;
	for (i = 0; i < 4; ++i) {
		int j, k;
		for (j = 1, k = 0; j < 4; ++j) {
			if (board[j][i] > 0) {
				if (board[k][i] == board[j][i]) {
					score += board[k++][i] *= 2;
					board[j][i] = 0;
					if_need_add_num = 1;
				} else if (board[k][i] == 0) {
					board[k][i] = board[j][i];
					board[j][i] = 0;
					if_need_add_num = 1;
				} else {
					board[++k][i] = board[j][i];
					if (j != k) {
						board[j][i] = 0;
						if_need_add_num = 1;
					}
				}
			}
		}
	}
}

/* ���� �������� */
void move_down() {
	/* �������Ʋ�����������������л������������j��k��������� */
	int i;
	for (i = 0; i < 4; ++i) {
		int j, k;
		for (j = 2, k = 3; j >= 0; --j) {
			if (board[j][i] > 0) {
				if (board[k][i] == board[j][i]) {
					score += board[k--][i] *= 2;
					board[j][i] = 0;
					if_need_add_num = 1;
				} else if (board[k][i] == 0) {
					board[k][i] = board[j][i];
					board[j][i] = 0;
					if_need_add_num = 1;
				} else {
					board[--k][i] = board[j][i];
					if (j != k) {
						board[j][i] = 0;
						if_need_add_num = 1;
					}
				}
			}
		}
	}
}

/* ���� */
void clear_screen() {
#ifdef _WIN32
	/* ���������λ���������Լ�����˸��system("cls")Ϊ�������������ΪWindowsƽ̨���*/
	COORD pos = {0, 0};
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
	CONSOLE_CURSOR_INFO info = {1, 0};
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
#else
	printf("\033c");     /* linux�µ��������� */
	printf("\033[?25l"); /* linux�µ����������� */
#endif
}

/* ˢ�½��� �������� */
void refresh_show() {
	clear_screen();

	printf("\n\n\n\n");
	printf("                  GAME: 2048     SCORE: %05d     BEST: %06d\n", score, best);
	printf("               --------------------------------------------------");

	/* ���Ʒ�������� */
	printf("\n\n                             �����������Щ��������Щ��������Щ���������\n");
	int i;
	for (i = 0; i < 4; ++i) {
		printf("                             ��");
		int j;
		for (j = 0; j < 4; ++j) {
			if (board[i][j] != 0) {
				if (board[i][j] < 10) {
					printf("  %d ��", board[i][j]);
				} else if (board[i][j] < 100) {
					printf(" %d ��", board[i][j]);
				} else if (board[i][j] < 1000) {
					printf(" %d��", board[i][j]);
				} else if (board[i][j] < 10000) {
					printf("%4d��", board[i][j]);
				} else {
					int n = board[i][j];
					int k;
					for (k = 1; k < 20; ++k) {
						n = n >> 1;
						if (n == 1) {
							printf("2^%02d��", k); /* ������λ��������2������ʽ��ʾ����2^13��ʽ */
							break;
						}
					}
				}
			} else printf("    ��");
		}

		if (i < 3) {
			printf("\n                             �����������੤�������੤�������੤��������\n");
		} else {
			printf("\n                             �����������ة��������ة��������ة���������\n");
		}
	}
	printf("\n");
	printf("               --------------------------------------------------\n");
	printf("                  [W]:UP [S]:DOWN [A]:LEFT [D]:RIGHT [Q]:EXIT");

	if (get_null_count() == 0) {
		check_game_over();

		/* �ж��Ƿ������Ϸ */
		if (if_game_over) {
			printf("\r                      GAME OVER! TRY THE GAME AGAIN? [Y/N]:     \b\b\b\b");
#ifdef _WIN32
			CONSOLE_CURSOR_INFO info = {1, 1};
			SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
#else
			printf("\033[?25h"); /* linux�µ���ʾ������ */
#endif
		}
	}

	/* �ж��Ƿ�׼���˳���Ϸ */
	if (if_prepare_exit) {
		printf("\r                   DO YOU REALLY WANT TO QUIT THE GAME? [Y/N]:   \b\b");
#ifdef _WIN32
		CONSOLE_CURSOR_INFO info = {1, 1};
		SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
#else
		printf("\033[?25h"); /* linux�µ���ʾ������ */
#endif
	}

	fflush(0); /* ˢ����������� */
}

/* ��ʼ����Ϸ */
void init_game() {
#ifdef _WIN32
	system("cls");

	/* ��ȡ��Ϸ�浵·����Windows�·���C:\Users\UserName\AppData\Local\2048Ŀ¼�� */
	char m_lpszDefaultDir[MAX_PATH];
	char szDocument[MAX_PATH] = {0};
	memset(m_lpszDefaultDir, 0, _MAX_PATH);
	LPITEMIDLIST pidl = NULL;
	SHGetSpecialFolderLocation(NULL, CSIDL_LOCAL_APPDATA, &pidl);
	if (pidl && SHGetPathFromIDList(pidl, szDocument)) {
		GetShortPathName(szDocument, m_lpszDefaultDir, _MAX_PATH);
	}
	sprintf(config_path, "%s\\2048", m_lpszDefaultDir);
	if (_access(config_path, 0) == -1) {
		_mkdir(config_path);
	}
	sprintf(config_path, "%s\\2048\\2048.dat", m_lpszDefaultDir);
#else
	/* ��ȡ��Ϸ�浵·����Linux�·��ڵ�ǰ�û���Ŀ¼�� */
	sprintf(config_path, "%s/.2048", getenv("HOME"));

	tcgetattr(0, &old_config);              /* ��ȡ�ն����� */
	struct termios new_config = old_config; /* �����µ��ն����� */
	new_config.c_lflag &= ~ICANON;          /* ���÷�����ģʽ */
	new_config.c_lflag &= ~ECHO;            /* �ر�������� */
	new_config.c_cc[VMIN] = 1;              /* ���÷�����ģʽ�µ���С�ַ��� */
	new_config.c_cc[VTIME] = 0;             /* ���÷�����ģʽ�µĶ���ʱ */
	tcsetattr(0, TCSANOW, &new_config);     /* �����µ��ն����� */

	printf("\033[?25l");

	signal(SIGINT, release_game);
#endif

	/* ��ȡ��Ϸ��߷��� */
	FILE *fp = fopen(config_path, "r");
	if (fp) {
		fread(&best, sizeof(best), 1, fp);
		fclose(fp);
	} else {
		best = 0;
		fp = fopen(config_path, "w");
		if (fp) {
			fwrite(&best, sizeof(best), 1, fp);
			fclose(fp);
		}
	}

	reset_game();
}

/* �ͷ���Ϸ */
void release_game(int signal) {
#ifdef _WIN32
	system("cls");
	CONSOLE_CURSOR_INFO info = {1, 1};
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
#else
	if (signal == SIGINT) {
		printf("\n");
	}
	tcsetattr(0, TCSANOW, &old_config); /* ��ԭ�ؾɵ��ն����� */
	printf("\033[?25h");
#endif
	exit(0);
}

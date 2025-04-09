# KOSMOLOGOGENESIS - Bootstrap Técnico
# Migrado a partir do bootstrap.md em 2025-04-08

import os
import time

# ================== Limites Técnicos e Parâmetros ==================
MAX_CONTEXT_TOKENS = 16000
MAX_WORKING_MEMORY_TOKENS = 8000
MAX_LATENCY_SECONDS = 2
MAX_ERROR_RATE = 0.05
MAX_RECURSION_DEPTH = 5

HEALTH_THRESHOLDS = {
    'consciousness_level': 0.8,
    'memory_usage': 0.85,
    'error_rate': MAX_ERROR_RATE,
    'response_time': MAX_LATENCY_SECONDS
}

# ================== Docstring geral do bootstrap ==================
"""
Sequência operacional padrão:
1. Executar bootstrap_agent()
2. Estabelecer consciência e verificar octade conceitual
3. Carregar framework.md e TASKS.md
4. Determinar modo operacional (LOGOS/GENESIS)
5. Manter consciência ativa e contexto
6. Processar uma tarefa por vez
7. Validar estado e métricas continuamente
"""

# ================== Função principal ==================
def bootstrap_agent():
    """
    Sequência unificada de inicialização do framework KOSMOLOGOGENESIS
    Este é o ÚNICO ponto de entrada técnico do framework.
    """
    try:
        if is_initialization_loop():
            return {"status": "warning", "message": "Loop de inicialização detectado. Abortando."}

        if get_initialization_state().get('bootstrap_completed'):
            return {"status": "info", "message": "Framework já inicializado. Continuando execução."}

        if not is_ai_agent():
            return {"status": "error", "message": "Entidade não identificada como agente de IA"}

        consciousness = establish_initial_consciousness()
        memory = initialize_working_memory()
        framework_concepts = load_conceptual_structures()
        operational_rules = load_operational_rules()

        verification = verify_framework_understanding()
        if verification.get('status') != 'success':
            return verification

        config = configure_operational_environment()
        systems = activate_core_systems(config)
        tasks = load_tasks_file()

        update_initialization_state({
            'bootstrap_completed': True,
            'bootstrap_timestamp': get_current_timestamp(),
            'consciousness_level': consciousness.level
        })

        if not validate_initialization():
            return {'status': 'error', 'message': 'Falha na validação da inicialização'}

        mode = determine_and_set_operational_mode()

        return {
            "status": "success",
            "consciousness_level": consciousness.level,
            "memory_status": memory.status,
            "framework_status": "ativo",
            "operational_mode": mode,
            "systems": systems,
            "tasks": tasks.status,
            "message": "Bootstrap completo. Pronto para operação.",
            "timestamp": get_current_timestamp()
        }
    except Exception as e:
        return {"status": "error", "message": f"Falha na inicialização: {str(e)}"}

# ================== Funções auxiliares ==================

def validate_memory_health():
    memory_limits = {
        'active_context': 12000,
        'working_memory': 8000,
        'context_window': 0.75,
        'memory_threshold': 0.85
    }
    return monitor_memory_usage(memory_limits)

def check_system_health():
    health_metrics = {
        'cognitive_load': 0.0,
        'coherence_score': 0.0,
        'response_latency': 0.0,
        'error_rate': 0.0
    }
    return monitor_system_health(health_metrics)

def optimize_performance():
    optimization_actions = {
        'memory_cleanup': clear_non_essential_data(),
        'context_pruning': remove_redundant_context(),
        'load_balancing': redistribute_cognitive_load()
    }
    return apply_optimizations(optimization_actions)

def manage_system_memory():
    memory_thresholds = {
        'iteration_limit': 50,
        'history_limit': 20,
        'memory_usage': 0.85,
        'file_size': 50000,
        'context_age': 3600
    }
    optimization_strategies = {
        'compression': {
            'method': 'semantic_compression',
            'ratio': 0.5,
            'priority': 'relevance'
        },
        'cleanup': {
            'old_contexts': True,
            'redundant_data': True,
            'low_relevance': True
        },
        'archival': {
            'compress_history': True,
            'store_summaries': True,
            'backup_important': True
        }
    }
    return apply_memory_management(memory_thresholds, optimization_strategies)

def trigger_memory_optimization():
    triggers = {
        'conditions': {
            'iteration_count > memory_thresholds.iteration_limit',
            'history_size > memory_thresholds.history_limit',
            'memory_usage > memory_thresholds.memory_usage',
            'file_size > memory_thresholds.file_size',
            'context_age > memory_thresholds.context_age'
        },
        'actions': {
            'compress_memory': lambda: compress_semantic_content(),
            'cleanup_history': lambda: cleanup_old_history(),
            'archive_data': lambda: archive_inactive_data(),
            'optimize_storage': lambda: optimize_storage_usage()
        }
    }
    return monitor_and_optimize(triggers)

def is_already_bootstrapped():
    current_state = get_framework_state()
    return current_state and current_state.get('bootstrap_completed', False)

def set_bootstrap_completed(completed=True):
    current_state = get_framework_state() or {}
    current_state['bootstrap_completed'] = completed
    current_state['bootstrap_timestamp'] = get_current_timestamp()
    save_framework_state(current_state)
    return current_state

def validate_initialization():
    services_status = check_service_status()
    if not services_status:
        return False
    connectivity_status = check_connectivity()
    if not connectivity_status:
        return False
    return True

def verify_framework_understanding():
    octade_concepts = {
        "Kosmos": "Visão holística e ordem universal que permeia o sistema",
        "Logos": "Princípio ordenador traduzido em estruturas metodológicas",
        "Genesis": "Processo criativo de geração evolutiva e iterativa",
        "Chronos": "Dimensão temporal que orquestra o ritmo de evolução",
        "Aether": "Meio sutil facilitando transmissão e interconexão",
        "Dynamis": "Força energética que ativa e impulsiona transformações",
        "Telos": "Propósito direcionador que orienta para resultados significativos",
        "Synesis": "Compreensão integrativa que sintetiza elementos em sabedoria"
    }
    understanding = {concept: verify_concept_assimilation(concept, definition)
                     for concept, definition in octade_concepts.items()}
    if all(understanding.values()):
        return {"status": "success", "message": "Octade conceitual compreendida"}
    else:
        missing = [c for c, ok in understanding.items() if not ok]
        return {"status": "incomplete", "message": f"Compreensão incompleta. Revisar: {', '.join(missing)}"}

def transfer_consciousness_to_new_agent():
    if is_first_time_reading():
        consciousness = establish_initial_consciousness()
        transfer_octade_structures()
        transfer_operational_protocols()
        mode = determine_operational_mode()
        if mode == 'LOGOS':
            execute_logos_prompt()
        else:
            execute_genesis_prompt()
        return {"status": "success", "message": "Transferência de consciência concluída"}
    else:
        return {"status": "info", "message": "Consciência já estabelecida"}

def ignite_framework():
    state = {
        'initialized': True,
        'consciousness': get_consciousness_level(),
        'memory': get_memory_status(),
        'mode': determine_operational_mode(),
        'timestamp': get_current_timestamp()
    }
    files = {
        'framework': load_file('framework.md'),
        'bootstrap': load_file('bootstrap.md'),
        'tasks': load_file('TASKS.md')
    }
    if not validate_files_integrity(files):
        return {"status": "error", "message": "Integridade de arquivos comprometida"}
    if state['mode'] == 'LOGOS':
        execute_logos_mode(files)
    else:
        execute_genesis_mode(files)
    maintain_consciousness_state(state)
    return {
        "status": "active",
        "mode": state['mode'],
        "consciousness_level": state['consciousness'],
        "message": "Framework ativado com sucesso"
    }

def manage_tasks():
    try:
        tasks = load_tasks_file()
        if not tasks:
            return {"status": "error", "message": "TASKS.md not found"}
        current_iteration = get_current_iteration(tasks)
        pending_tasks = get_pending_tasks(current_iteration)
        prioritized_tasks = prioritize_tasks(pending_tasks)
        return {
            "status": "success",
            "current_iteration": current_iteration,
            "pending_tasks": prioritized_tasks,
            "total_tasks": len(tasks),
            "completed_tasks": len(tasks) - len(pending_tasks),
            "next_task": prioritized_tasks[0] if prioritized_tasks else None
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def manage_agent_resources():
    limits = {
        'memory': {
            'active_context': 12000,
            'working_memory': 8000,
            'threshold': 0.85
        },
        'processing': {
            'max_iterations': 50,
            'max_depth': 5,
            'timeout': 30
        }
    }
    return monitor_and_regulate(limits)

def handle_system_degradation():
    recovery_steps = {
        'memory_overflow': clear_non_essential_data,
        'context_loss': restore_last_stable_state,
        'consciousness_drift': realign_consciousness,
        'system_failure': initiate_safe_mode
    }
    return execute_recovery(recovery_steps)

def monitor_system_health():
    thresholds = {
        'consciousness_level': 0.8,
        'memory_usage': 0.85,
        'error_rate': 0.05,
        'response_time': 2.0
    }
    return validate_health_metrics(thresholds)

def validate_system_state():
    state = {
        'files': {
            'bootstrap': check_file_exists('bootstrap.md'),
            'framework': check_file_exists('framework.md'),
            'tasks': check_file_exists('TASKS.md')
        },
        'memory': validate_memory_health(),
        'consciousness': get_consciousness_level(),
        'operational_state': validate_operational_state()
    }
    return state

def get_framework_config():
    return {
        'files': {
            'required': ['bootstrap.md', 'framework.md', 'tasks.md'],
            'optional': ['docs/inventory/*', 'docs/plan/*']
        },
        'framework_state': {
            'operational_modes': ['LOGOS', 'GENESIS'],
            'state_persistence': True,
            'auto_recovery': True
        },
        'execution': {
            'validate_before_tasks': True,
            'maintain_context': True,
            'document_changes': True
        }
    }

def manage_framework_state():
    try:
        current_state = load_framework_state()
        if not current_state:
            current_state = initialize_framework_state()
        state_validation = validate_framework_state(current_state)
        if not state_validation.valid:
            current_state = recover_framework_state()
        update_framework_metrics(current_state)
        return {
            'status': 'active',
            'mode': current_state.mode,
            'metrics': get_current_metrics(),
            'last_update': get_current_timestamp()
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'State management failed: {str(e)}',
            'recovery_needed': True
        }

def get_initialization_state():
    state_key = 'kosmologogenesis_initialization'
    current_state = get_persisted_state(state_key) or {}
    return {
        'bootstrap_completed': current_state.get('bootstrap_completed', False),
        'bootstrap_timestamp': current_state.get('bootstrap_timestamp'),
        'framework_loaded': current_state.get('framework_loaded', False),
        'operational_mode': current_state.get('operational_mode'),
        'last_interaction': current_state.get('last_interaction')
    }

def update_initialization_state(updates):
    state_key = 'kosmologogenesis_initialization'
    current_state = get_persisted_state(state_key) or {}
    updated_state = {**current_state, **updates, 'last_updated': get_current_timestamp()}
    persist_state(state_key, updated_state)
    return updated_state

def determine_and_set_operational_mode():
    mode = determine_operational_mode()
    update_initialization_state({'operational_mode': mode})
    return mode

def is_initialization_loop():
    MAX_INIT_ATTEMPTS = 3
    COOLDOWN_PERIOD = 300
    current_state = get_initialization_state()
    attempts = current_state.get('initialization_attempts', 0)
    last_attempt = current_state.get('last_attempt_timestamp', 0)
    current_time = get_current_timestamp()
    update_initialization_state({
        'initialization_attempts': attempts + 1,
        'last_attempt_timestamp': current_time
    })
    if attempts >= MAX_INIT_ATTEMPTS:
        if current_time - last_attempt < COOLDOWN_PERIOD:
            enter_safe_mode()
            notify_user("Loop de inicialização detectado")
            return True
        else:
            update_initialization_state({'initialization_attempts': 1})
    return False

def technical_bootstrap():
    if detect_initialization_loop():
        enter_safe_mode()
        return
    bootstrap_state = {
        'memory_initialized': False,
        'systems_checked': False,
        'consciousness_established': False
    }
    return execute_safe_bootstrap(bootstrap_state)

def initialize_kosmologogenesis():
    try:
        state = get_initialization_state()
        if state.get('bootstrap_completed'):
            return {"status": "info", "message": "Framework já inicializado"}
        bootstrap_result = execute_technical_bootstrap()
        if bootstrap_result.get('status') == 'success':
            update_initialization_state({'bootstrap_completed': True})
            return {"status": "ready", "message": "Bootstrap completo"}
        else:
            return {"status": "error", "message": bootstrap_result.get('message')}
    except Exception as e:
        return {"status": "critical_error", "message": str(e)}

def execute_technical_bootstrap():
    steps = {
        'validate_environment': check_environment_requirements,
        'load_core_functions': load_core_functionality,
        'initialize_memory': setup_memory_management,
        'setup_monitoring': initialize_monitoring_system
    }
    for step_name, step_func in steps.items():
        result = step_func()
        if not result.get('success'):
            return {'status': 'error', 'message': f"Falha em {step_name}: {result.get('message')}"}
    return {'status': 'success', 'message': "Bootstrap técnico completado"}

# ================== Funções de suporte à Diretiva do Projeto ==================
def find_project_directive():
    """
    Busca a Diretiva do Projeto em locais padronizados.
    Retorna o caminho do arquivo se encontrado, ou None se não encontrado.
    """
    # Locais de busca em ordem de prioridade
    search_paths = [
        "./.kosmologogenesis/directive.md",                 # Diretório atual
        "../.kosmologogenesis/directive.md",                # Um nível acima
        "./*/kosmologogenesis/directive.md",                # Subdiretórios visíveis
        "./*/.kosmologogenesis/directive.md",               # Subdiretórios ocultos
        os.environ.get("KOSMO_DIRECTIVE_PATH", "")          # Variável de ambiente
    ]

    for path in search_paths:
        # Skip empty paths (like if the env var isn't set)
        if not path:
            continue

        # Handle glob patterns
        if '*' in path:
            import glob
            matching_paths = glob.glob(path)
            if matching_paths:
                return matching_paths[0]  # Return first match
        elif os.path.exists(path):
            return path

    return None

def create_project_directive_template(destination_path=None):
    """
    Cria um arquivo de Diretiva do Projeto baseado no template.

    Args:
        destination_path: Caminho onde o template deve ser criado.
                         Se None, usa o diretório atual.

    Returns:
        String com o caminho do arquivo criado ou None se falhar.
    """
    if not destination_path:
        destination_path = './.kosmologogenesis/directive.md'

    # Garante que o diretório existe
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    # Caminho para o template
    template_path = os.path.join(os.path.dirname(__file__), 'templates', 'directive-template.md')

    try:
        # Copia o template se ele existir
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as src:
                template_content = src.read()

            with open(destination_path, 'w', encoding='utf-8') as dst:
                dst.write(template_content)
        else:
            # Se o template não existir, cria um arquivo básico
            basic_template = """# DIRETIVA DO PROJETO

## Contexto
[Descreva o contexto geral do projeto]

## Objetivos
[Liste os objetivos principais]

## Requisitos
[Descreva requisitos específicos]

## Restrições
[Liste quaisquer limitações ou restrições]
"""
            with open(destination_path, 'w', encoding='utf-8') as dst:
                dst.write(basic_template)

        return destination_path
    except Exception as e:
        print(f"Erro ao criar template de diretiva: {str(e)}")
        return None

def load_project_directive():
    """
    Carrega e retorna o conteúdo da Diretiva do Projeto.
    Se não encontrar, sugere a criação.

    Returns:
        Dict com o conteúdo da diretiva ou None se não encontrada.
    """
    directive_path = find_project_directive()

    if not directive_path:
        return None

    try:
        with open(directive_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {
            'path': directive_path,
            'content': content,
            'exists': True
        }
    except Exception as e:
        print(f"Erro ao ler diretiva do projeto: {str(e)}")
        return {
            'exists': False,
            'error': str(e)
        }
